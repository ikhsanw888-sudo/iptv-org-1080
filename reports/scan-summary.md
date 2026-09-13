# iptv-org 1080 Scan Summary

- Streams tested: **17245**
- PASS: **12170**
- REVIEW: **3336**
- FAIL: **1736**
- Eligible HLS at least 1080 lines before deduplication: **4630**
- Unique channels selected: **3531**
- STB-safe channels without special HTTP headers: **3266**

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
| Auto | 7 |
| Business | 24 |
| Classic | 8 |
| Comedy | 17 |
| Cooking | 11 |
| Culture | 42 |
| Documentary | 72 |
| Education | 55 |
| Entertainment | 189 |
| Family | 19 |
| General | 714 |
| Kids | 78 |
| Legislative | 37 |
| Lifestyle | 39 |
| Movies | 161 |
| Music | 270 |
| News | 335 |
| Outdoor | 24 |
| Public | 1 |
| Relax | 2 |
| Religious | 226 |
| Science | 7 |
| Series | 68 |
| Shop | 17 |
| Sports | 147 |
| Travel | 18 |
| Unclassified | 926 |
| Weather | 5 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
