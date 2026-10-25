# iptv-org 1080 Scan Summary

- Streams tested: **18056**
- PASS: **12615**
- REVIEW: **3703**
- FAIL: **1733**
- Eligible HLS at least 1080 lines before deduplication: **4696**
- Unique channels selected: **3597**
- STB-safe channels without special HTTP headers: **3406**

## Outputs

- `generated/iptv-org-1080.m3u`: all selected 1080 HLS channels
- `generated/iptv-org-1080-stb.m3u`: safer subset for older STBs
- `generated/genres/*.m3u`: one playlist per genre
- `reports/selected-1080.csv`: selected-channel audit table
- `reports/all-results.csv.gz`: complete scan report (workflow artifact)

## Channels by genre

| Genre | Channels |
|---|---:|
| Animation | 12 |
| Auto | 9 |
| Business | 28 |
| Classic | 8 |
| Comedy | 16 |
| Cooking | 17 |
| Culture | 39 |
| Documentary | 69 |
| Education | 51 |
| Entertainment | 194 |
| Family | 17 |
| General | 719 |
| Kids | 82 |
| Legislative | 33 |
| Lifestyle | 42 |
| Movies | 158 |
| Music | 281 |
| News | 372 |
| Outdoor | 26 |
| Public | 1 |
| Relax | 1 |
| Religious | 241 |
| Science | 6 |
| Series | 76 |
| Shop | 16 |
| Sports | 140 |
| Travel | 18 |
| Unclassified | 919 |
| Weather | 6 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
