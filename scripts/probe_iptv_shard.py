#!/usr/bin/env python3
"""Probe one shard of iptv-org streams with ffprobe."""

from __future__ import annotations

import argparse
import ipaddress
import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

REVIEW_MARKERS = (
    "401 unauthorized",
    "403 forbidden",
    "451 unavailable",
    "429 too many",
    "server returned 5",
    "temporary failure",
    "name or service not known",
    "connection timed out",
    "connection refused",
    "network is unreachable",
    "i/o error",
    "input/output error",
    "end of file",
    "http error 403",
    "http error 429",
)
SUPPORTED_SCHEMES = {"http", "https", "rtmp", "rtmps", "rtsp"}


def literal_private_host(hostname: str) -> bool:
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        return False
    return bool(
        address.is_private
        or address.is_loopback
        or address.is_link_local
        or address.is_multicast
        or address.is_reserved
    )


def classify_failure(stderr: str, timed_out: bool = False) -> str:
    text = stderr.lower()
    if timed_out or any(marker in text for marker in REVIEW_MARKERS):
        return "REVIEW"
    return "FAIL"


def classify_scan(field_order: str) -> str:
    value = (field_order or "").lower()
    if value == "progressive":
        return "p"
    if value in {"tt", "bb", "tb", "bt"}:
        return "i"
    return "unknown"


def run_ffprobe(record: dict[str, Any], timeout_seconds: int) -> dict[str, Any]:
    url = record["url"]
    parts = urlsplit(url)
    scheme = parts.scheme.lower()
    hostname = parts.hostname or ""

    result = dict(record)
    result.update(
        {
            "status": "FAIL",
            "http_compatible": scheme in {"http", "https"},
            "hls": False,
            "format_name": "",
            "width": 0,
            "height": 0,
            "scan": "unknown",
            "codec": "",
            "latency_ms": 0,
            "error": "",
        }
    )

    if scheme not in SUPPORTED_SCHEMES:
        result["status"] = "SKIP_PROTOCOL"
        result["error"] = f"Unsupported protocol: {scheme or 'missing'}"
        return result

    if literal_private_host(hostname):
        result["status"] = "SKIP_PRIVATE"
        result["error"] = "Literal private, loopback, or reserved IP address"
        return result

    command = [
        "ffprobe",
        "-v",
        "error",
        "-hide_banner",
        "-rw_timeout",
        str(timeout_seconds * 1_000_000),
        "-analyzeduration",
        "5000000",
        "-probesize",
        "5000000",
    ]

    if record.get("user_agent"):
        command.extend(["-user_agent", record["user_agent"]])
    if record.get("referrer"):
        command.extend(["-headers", f"Referer: {record['referrer']}\r\n"])

    command.extend(
        [
            "-show_entries",
            (
                "stream=index,codec_type,codec_name,width,height,"
                "coded_width,coded_height,field_order:"
                "format=format_name,duration"
            ),
            "-of",
            "json",
            url,
        ]
    )

    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout_seconds + 5,
            check=False,
        )
    except subprocess.TimeoutExpired:
        result["status"] = "REVIEW"
        result["latency_ms"] = round((time.monotonic() - started) * 1000)
        result["error"] = f"ffprobe timed out after {timeout_seconds + 5}s"
        return result
    except OSError as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"
        return result

    result["latency_ms"] = round((time.monotonic() - started) * 1000)
    if completed.returncode != 0:
        stderr = (completed.stderr or "").strip()
        result["status"] = classify_failure(stderr)
        result["error"] = stderr[-1000:] or f"ffprobe exited with {completed.returncode}"
        return result

    try:
        payload = json.loads(completed.stdout or "{}")
    except json.JSONDecodeError as exc:
        result["error"] = f"Invalid ffprobe JSON: {exc}"
        return result

    video_streams = [
        stream
        for stream in payload.get("streams", [])
        if stream.get("codec_type") == "video"
    ]
    if not video_streams:
        result["error"] = "No video stream detected"
        return result

    def stream_height(stream: dict[str, Any]) -> int:
        return int(stream.get("height") or stream.get("coded_height") or 0)

    best_video = max(video_streams, key=stream_height)
    height = stream_height(best_video)
    width = int(best_video.get("width") or best_video.get("coded_width") or 0)
    format_name = (payload.get("format") or {}).get("format_name") or ""
    hls = "hls" in format_name.lower() or ".m3u8" in parts.path.lower()

    result.update(
        {
            "status": "PASS",
            "hls": hls,
            "format_name": format_name,
            "width": width,
            "height": height,
            "scan": classify_scan(best_video.get("field_order") or ""),
            "codec": best_video.get("codec_name") or "",
            "error": "",
        }
    )
    return result


def probe_with_retries(
    record: dict[str, Any],
    timeout_seconds: int,
    attempts: int,
) -> dict[str, Any]:
    last_result: dict[str, Any] | None = None
    for attempt in range(1, attempts + 1):
        result = run_ffprobe(record, timeout_seconds)
        result["attempts"] = attempt
        last_result = result
        if result["status"] == "PASS":
            return result
        if attempt < attempts:
            time.sleep(2)
    assert last_result is not None
    return last_result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--timeout", type=int, default=18)
    parser.add_argument("--attempts", type=int, default=2)
    args = parser.parse_args()

    records = json.loads(Path(args.input).read_text(encoding="utf-8"))
    results: list[dict[str, Any]] = []

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_map = {
            executor.submit(
                probe_with_retries,
                record,
                args.timeout,
                args.attempts,
            ): record
            for record in records
        }
        for count, future in enumerate(as_completed(future_map), start=1):
            record = future_map[future]
            try:
                result = future.result()
            except Exception as exc:
                result = dict(record)
                result.update(
                    {
                        "status": "FAIL",
                        "http_compatible": False,
                        "hls": False,
                        "format_name": "",
                        "width": 0,
                        "height": 0,
                        "scan": "unknown",
                        "codec": "",
                        "latency_ms": 0,
                        "attempts": 1,
                        "error": f"Unhandled tester error: {type(exc).__name__}: {exc}",
                    }
                )
            results.append(result)
            print(
                f"[{count:04d}/{len(records):04d}] "
                f"{result['status']:<13} "
                f"{result.get('height', 0):>4} "
                f"{result.get('name', '')}"
            )

    results.sort(key=lambda item: int(item.get("source_index", 0)))
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        for result in results:
            file.write(json.dumps(result, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
