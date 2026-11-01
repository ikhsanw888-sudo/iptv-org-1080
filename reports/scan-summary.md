# iptv-org 1080 Scan Summary

- Streams tested: **18434**
- PASS: **13150**
- REVIEW: **3565**
- FAIL: **1714**
- Eligible HLS at least 1080 lines before deduplication: **4827**
- Unique channels selected: **3697**
- STB-safe channels without special HTTP headers: **3443**

## Outputs

- `generated/iptv-org-1080.m3u`: all selected 1080 HLS channels
- `generated/iptv-org-1080-stb.m3u`: safer subset for older STBs
- `generated/genres/*.m3u`: one playlist per genre
- `reports/selected-1080.csv`: selected-channel audit table
- `reports/all-results.csv.gz`: complete scan report (workflow artifact)

## Channels by genre

| Genre | Channels |
|---|---:|
| Animation | 11 |
| Auto | 9 |
| Business | 26 |
| Classic | 8 |
| Comedy | 15 |
| Cooking | 18 |
| Culture | 39 |
| Documentary | 80 |
| Education | 49 |
| Entertainment | 206 |
| Family | 17 |
| General | 723 |
| Kids | 82 |
| Legislative | 31 |
| Lifestyle | 43 |
| Movies | 175 |
| Music | 284 |
| News | 368 |
| Outdoor | 26 |
| Public | 1 |
| Relax | 1 |
| Religious | 246 |
| Science | 6 |
| Series | 76 |
| Shop | 17 |
| Sports | 165 |
| Travel | 22 |
| Unclassified | 947 |
| Weather | 6 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
