# iptv-org 1080 Scan Summary

- Streams tested: **17786**
- PASS: **12807**
- REVIEW: **3188**
- FAIL: **1788**
- Eligible HLS at least 1080 lines before deduplication: **4922**
- Unique channels selected: **3711**
- STB-safe channels without special HTTP headers: **3472**

## Outputs

- `generated/iptv-org-1080.m3u`: all selected 1080 HLS channels
- `generated/iptv-org-1080-stb.m3u`: safer subset for older STBs
- `generated/genres/*.m3u`: one playlist per genre
- `reports/selected-1080.csv`: selected-channel audit table
- `reports/all-results.csv.gz`: complete scan report (workflow artifact)

## Channels by genre

| Genre | Channels |
|---|---:|
| Animation | 13 |
| Auto | 6 |
| Business | 26 |
| Classic | 8 |
| Comedy | 18 |
| Cooking | 14 |
| Culture | 39 |
| Documentary | 67 |
| Education | 55 |
| Entertainment | 198 |
| Family | 17 |
| General | 780 |
| Kids | 84 |
| Legislative | 40 |
| Lifestyle | 38 |
| Movies | 153 |
| Music | 273 |
| News | 332 |
| Outdoor | 25 |
| Relax | 2 |
| Religious | 233 |
| Science | 9 |
| Series | 65 |
| Shop | 18 |
| Sports | 160 |
| Travel | 16 |
| Unclassified | 1018 |
| Weather | 4 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
