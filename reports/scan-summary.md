# iptv-org 1080 Scan Summary

- Streams tested: **16984**
- PASS: **12108**
- REVIEW: **3497**
- FAIL: **1376**
- Eligible HLS at least 1080 lines before deduplication: **4591**
- Unique channels selected: **3583**
- STB-safe channels without special HTTP headers: **3330**

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
| Auto | 5 |
| Business | 23 |
| Classic | 8 |
| Comedy | 16 |
| Cooking | 14 |
| Culture | 40 |
| Documentary | 77 |
| Education | 55 |
| Entertainment | 190 |
| Family | 15 |
| General | 745 |
| Kids | 78 |
| Legislative | 37 |
| Lifestyle | 36 |
| Movies | 143 |
| Music | 267 |
| News | 337 |
| Outdoor | 24 |
| Public | 1 |
| Relax | 2 |
| Religious | 236 |
| Science | 7 |
| Series | 65 |
| Shop | 17 |
| Sports | 155 |
| Travel | 16 |
| Unclassified | 956 |
| Weather | 6 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
