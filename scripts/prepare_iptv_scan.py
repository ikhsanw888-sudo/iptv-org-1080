#!/usr/bin/env python3
"""Download current iptv-org metadata, enrich streams, remove exact URL
repeats, and split the scan into balanced GitHub Actions shards.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

API_BASE = "https://iptv-org.github.io/api"
USER_AGENT = "iptv-org-1080-workflow/1.0 (+GitHub Actions)"


def download_json(name: str) -> list[dict[str, Any]]:
    request = Request(
        f"{API_BASE}/{name}.json",
        headers={"User-Agent": USER_AGENT},
    )
    with urlopen(request, timeout=90) as response:
        return json.load(response)


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


def choose_logo(
    channel_id: str | None,
    feed_id: str | None,
    exact_logo: dict[tuple[str, str], str],
    channel_logo: dict[str, str],
) -> str:
    if channel_id and feed_id:
        logo = exact_logo.get((channel_id, feed_id))
        if logo:
            return logo
    return channel_logo.get(channel_id or "", "")


def richness(record: dict[str, Any]) -> tuple[int, int, int]:
    return (
        1 if record.get("channel_id") else 0,
        1 if record.get("name") else 0,
        1 if not record.get("label") else 0,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="work")
    parser.add_argument("--shards", type=int, default=24)
    args = parser.parse_args()

    if not 1 <= args.shards <= 256:
        raise SystemExit("--shards must be between 1 and 256")

    print("Downloading current iptv-org API data...")
    streams = download_json("streams")
    channels = download_json("channels")
    feeds = download_json("feeds")
    logos = download_json("logos")
    categories = download_json("categories")
    countries = download_json("countries")
    blocklist = download_json("blocklist")

    channel_by_id = {item["id"]: item for item in channels}
    category_by_id = {item["id"]: item["name"] for item in categories}
    country_by_code = {item["code"]: item for item in countries}
    blocked_ids = {item["channel"] for item in blocklist}
    feed_by_key = {(item["channel"], item["id"]): item for item in feeds}

    exact_logo: dict[tuple[str, str], str] = {}
    channel_logo: dict[str, str] = {}
    for logo in logos:
        if not logo.get("in_use"):
            continue
        channel_id = logo.get("channel")
        feed_id = logo.get("feed")
        logo_url = logo.get("url") or ""
        if channel_id and feed_id:
            exact_logo.setdefault((channel_id, feed_id), logo_url)
        elif channel_id:
            channel_logo.setdefault(channel_id, logo_url)

    enriched: list[dict[str, Any]] = []
    for index, stream in enumerate(streams):
        url = (stream.get("url") or "").strip()
        if not url:
            continue

        channel_id = stream.get("channel")
        feed_id = stream.get("feed")
        channel = channel_by_id.get(channel_id, {}) if channel_id else {}
        feed = feed_by_key.get((channel_id, feed_id), {}) if channel_id and feed_id else {}

        category_ids = list(channel.get("categories") or [])
        category_names = [
            category_by_id.get(category_id, category_id.title())
            for category_id in category_ids
        ]

        country_code = channel.get("country") or ""
        country = country_by_code.get(country_code, {})
        name = (
            stream.get("title")
            or feed.get("name")
            or channel.get("name")
            or f"Unmapped Stream {index + 1}"
        )

        enriched.append(
            {
                "source_index": index,
                "channel_id": channel_id or "",
                "feed_id": feed_id or "",
                "feed_is_main": bool(feed.get("is_main")),
                "name": name,
                "channel_name": channel.get("name") or name,
                "url": url,
                "normalized_url": normalize_url(url),
                "referrer": stream.get("referrer") or "",
                "user_agent": stream.get("user_agent") or "",
                "quality_hint": stream.get("quality") or "",
                "label": stream.get("label") or "",
                "country_code": country_code,
                "country_name": country.get("name") or "",
                "country_flag": country.get("flag") or "",
                "category_ids": category_ids,
                "category_names": category_names,
                "is_nsfw": bool(channel.get("is_nsfw")),
                "closed": channel.get("closed") or "",
                "blocked": bool(channel_id and channel_id in blocked_ids),
                "logo": choose_logo(channel_id, feed_id, exact_logo, channel_logo),
            }
        )

    # Probe each exact URL once. If one URL has multiple mappings, retain the
    # richest mapped record because the final output removes URL duplicates.
    by_url: dict[str, dict[str, Any]] = {}
    for record in enriched:
        key = record["normalized_url"] or record["url"]
        current = by_url.get(key)
        if current is None or richness(record) > richness(current):
            by_url[key] = record

    unique_records = sorted(
        by_url.values(),
        key=lambda item: (
            item.get("country_code", ""),
            item.get("channel_name", "").lower(),
            item.get("normalized_url", ""),
        ),
    )

    output_dir = Path(args.output_dir)
    shard_dir = output_dir / "shards"
    shard_dir.mkdir(parents=True, exist_ok=True)

    shard_names = [f"{index:02d}" for index in range(args.shards)]
    shard_records: list[list[dict[str, Any]]] = [[] for _ in range(args.shards)]
    for index, record in enumerate(unique_records):
        shard_records[index % args.shards].append(record)

    for shard_name, records in zip(shard_names, shard_records):
        (shard_dir / f"shard-{shard_name}.json").write_text(
            json.dumps(records, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

    (output_dir / "matrix.json").write_text(
        json.dumps({"shard": shard_names}, separators=(",", ":")),
        encoding="utf-8",
    )
    summary = {
        "api_streams": len(streams),
        "unique_urls": len(unique_records),
        "shards": args.shards,
        "shard_sizes": [len(records) for records in shard_records],
    }
    (output_dir / "prepare-summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
