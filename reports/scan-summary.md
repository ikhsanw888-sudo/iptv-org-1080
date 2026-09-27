# iptv-org 1080 Scan Summary

- Streams tested: **17600**
- PASS: **12405**
- REVIEW: **3562**
- FAIL: **1630**
- Eligible HLS at least 1080 lines before deduplication: **4629**
- Unique channels selected: **3522**
- STB-safe channels without special HTTP headers: **3290**

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
| Auto | 6 |
| Business | 28 |
| Classic | 8 |
| Comedy | 16 |
| Cooking | 11 |
| Culture | 40 |
| Documentary | 75 |
| Education | 53 |
| Entertainment | 186 |
| Family | 14 |
| General | 695 |
| Kids | 78 |
| Legislative | 29 |
| Lifestyle | 37 |
| Movies | 161 |
| Music | 264 |
| News | 348 |
| Outdoor | 26 |
| Public | 1 |
| Relax | 2 |
| Religious | 240 |
| Science | 7 |
| Series | 67 |
| Shop | 17 |
| Sports | 147 |
| Travel | 20 |
| Unclassified | 929 |
| Weather | 5 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
