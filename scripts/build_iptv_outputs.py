#!/usr/bin/env python3
"""Merge shard results, select active 1080 HLS streams, remove duplicates,
and generate master and genre playlists.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

GENRE_PRIORITY = [
    "sports",
    "news",
    "business",
    "documentary",
    "science",
    "education",
    "kids",
    "family",
    "movies",
    "series",
    "music",
    "travel",
    "weather",
    "cooking",
    "culture",
    "lifestyle",
    "outdoor",
    "religious",
    "shop",
    "relax",
    "entertainment",
    "general",
]


def normalize_url(url: str) -> str:
    value = (url or "").strip()
    try:
        parts = urlsplit(value)
    except ValueError:
        return value
    scheme = parts.scheme.lower()
    hostname = (parts.hostname or "").lower()
    if not hostname:
        return value
    port = parts.port
    if (scheme == "http" and port == 80) or (scheme == "https" and port == 443):
        port = None
    netloc = hostname if port is None else f"{hostname}:{port}"
    return urlunsplit((scheme, netloc, parts.path, parts.query, ""))


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "unclassified"


def primary_genre(item: dict[str, Any]) -> str:
    ids = [str(value).lower() for value in item.get("category_ids", [])]
    names = item.get("category_names", [])
    paired = list(zip(ids, names))
    for preferred in GENRE_PRIORITY:
        for category_id, category_name in paired:
            if category_id == preferred:
                return category_name or preferred.title()
    return str(names[0]) if names else "Unclassified"


def channel_key(item: dict[str, Any]) -> str:
    channel_id = (item.get("channel_id") or "").strip()
    if channel_id:
        return f"channel:{channel_id.lower()}"
    name = item.get("channel_name") or item.get("name") or ""
    return f"unmapped:{slug(name)}"


def selection_score(item: dict[str, Any]) -> tuple[Any, ...]:
    scan = item.get("scan")
    scan_score = 2 if scan == "p" else 1 if scan == "unknown" else 0
    return (
        int(item.get("height") or 0),
        scan_score,
        1 if item.get("feed_is_main") else 0,
        0 if not item.get("label") else -1,
        0 if not (item.get("referrer") or item.get("user_agent")) else -1,
        1 if str(item.get("url", "")).startswith("https://") else 0,
        -int(item.get("latency_ms") or 999999),
    )


def esc(value: Any) -> str:
    return (
        str(value or "")
        .replace("\\", "")
        .replace('"', "'")
        .replace("\r", " ")
        .replace("\n", " ")
        .strip()
    )


def quality_label(item: dict[str, Any]) -> str:
    height = int(item.get("height") or 0)
    scan = item.get("scan") or "unknown"
    suffix = scan if scan in {"p", "i"} else ""
    return f"{height}{suffix}" if height else "unknown"


def m3u_lines(items: list[dict[str, Any]]) -> list[str]:
    lines = ["#EXTM3U"]
    for item in items:
        genre = esc(primary_genre(item))
        channel_id = esc(item.get("channel_id"))
        name = esc(item.get("channel_name") or item.get("name") or "Unknown")
        logo = esc(item.get("logo"))
        country = esc(item.get("country_code"))
        attrs = [
            f'tvg-id="{channel_id}"',
            f'tvg-name="{name}"',
            f'group-title="{genre}"',
        ]
        if logo:
            attrs.append(f'tvg-logo="{logo}"')
        if country:
            attrs.append(f'tvg-country="{country}"')
        lines.append(f'#EXTINF:-1 {" ".join(attrs)},{name} [{quality_label(item)}]')
        if item.get("referrer"):
            lines.append(f'#EXTVLCOPT:http-referrer={item["referrer"]}')
        if item.get("user_agent"):
            lines.append(f'#EXTVLCOPT:http-user-agent={item["user_agent"]}')
        lines.append(item["url"])
    return lines


def write_m3u(path: Path, items: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(m3u_lines(items)) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", default="generated")
    parser.add_argument("--report-dir", default="reports")
    parser.add_argument("--min-height", type=int, default=1080)
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    report_dir = Path(args.report_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, Any]] = []
    for path in sorted(input_dir.glob("result-*.jsonl")):
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    results.append(json.loads(line))
    if not results:
        raise SystemExit("No shard results found")

    full_fields = [
        "status", "channel_id", "feed_id", "name", "channel_name",
        "country_code", "category_ids", "url", "quality_hint", "height",
        "width", "scan", "codec", "hls", "format_name", "latency_ms",
        "attempts", "label", "referrer", "user_agent", "is_nsfw",
        "blocked", "closed", "error",
    ]
    with gzip.open(report_dir / "all-results.csv.gz", "wt", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=full_fields)
        writer.writeheader()
        for item in results:
            row = {field: item.get(field, "") for field in full_fields}
            row["category_ids"] = "|".join(item.get("category_ids", []))
            writer.writerow(row)

    eligible = [
        item for item in results
        if item.get("status") == "PASS"
        and bool(item.get("hls"))
        and int(item.get("height") or 0) >= args.min_height
        and not item.get("is_nsfw")
        and not item.get("blocked")
        and not item.get("closed")
    ]

    best_by_url: dict[str, dict[str, Any]] = {}
    for item in eligible:
        key = normalize_url(item["url"])
        current = best_by_url.get(key)
        if current is None or selection_score(item) > selection_score(current):
            best_by_url[key] = item

    best_by_channel: dict[str, dict[str, Any]] = {}
    for item in best_by_url.values():
        key = channel_key(item)
        current = best_by_channel.get(key)
        if current is None or selection_score(item) > selection_score(current):
            best_by_channel[key] = item

    selected = list(best_by_channel.values())
    selected.sort(key=lambda item: (
        primary_genre(item).lower(),
        (item.get("country_code") or "").lower(),
        (item.get("channel_name") or item.get("name") or "").lower(),
    ))
    stb_safe = [
        item for item in selected
        if not item.get("referrer") and not item.get("user_agent")
    ]

    write_m3u(output_dir / "iptv-org-1080.m3u", selected)
    write_m3u(output_dir / "iptv-org-1080-stb.m3u", stb_safe)

    by_genre: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in selected:
        by_genre[primary_genre(item)].append(item)
    for genre, items in sorted(by_genre.items()):
        write_m3u(output_dir / "genres" / f"{slug(genre)}.m3u", items)

    selected_fields = [
        "channel_id", "name", "country", "genre", "quality", "codec",
        "url", "requires_headers", "label", "latency_ms",
    ]
    with (report_dir / "selected-1080.csv").open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=selected_fields)
        writer.writeheader()
        for item in selected:
            writer.writerow({
                "channel_id": item.get("channel_id") or "",
                "name": item.get("channel_name") or item.get("name") or "",
                "country": item.get("country_code") or "",
                "genre": primary_genre(item),
                "quality": quality_label(item),
                "codec": item.get("codec") or "",
                "url": item["url"],
                "requires_headers": bool(item.get("referrer") or item.get("user_agent")),
                "label": item.get("label") or "",
                "latency_ms": item.get("latency_ms") or 0,
            })

    status_counts = Counter(item.get("status", "UNKNOWN") for item in results)
    genre_counts = Counter(primary_genre(item) for item in selected)
    summary = [
        "# iptv-org 1080 Scan Summary", "",
        f"- Streams tested: **{len(results)}**",
        f"- PASS: **{status_counts.get('PASS', 0)}**",
        f"- REVIEW: **{status_counts.get('REVIEW', 0)}**",
        f"- FAIL: **{status_counts.get('FAIL', 0)}**",
        f"- Eligible HLS at least {args.min_height} lines before deduplication: **{len(eligible)}**",
        f"- Unique channels selected: **{len(selected)}**",
        f"- STB-safe channels without special HTTP headers: **{len(stb_safe)}**",
        "", "## Outputs", "",
        "- `generated/iptv-org-1080.m3u`: all selected 1080 HLS channels",
        "- `generated/iptv-org-1080-stb.m3u`: safer subset for older STBs",
        "- `generated/genres/*.m3u`: one playlist per genre",
        "- `reports/selected-1080.csv`: selected-channel audit table",
        "- `reports/all-results.csv.gz`: complete scan report (workflow artifact)",
        "", "## Channels by genre", "", "| Genre | Channels |", "|---|---:|",
    ]
    for genre, count in sorted(genre_counts.items()):
        summary.append(f"| {genre} | {count} |")
    summary += [
        "",
        "> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.",
        "",
    ]
    (report_dir / "scan-summary.md").write_text("\n".join(summary), encoding="utf-8")
    print("\n".join(summary[:10]))


if __name__ == "__main__":
    main()
