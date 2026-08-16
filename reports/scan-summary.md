# iptv-org 1080 Scan Summary

- Streams tested: **16613**
- PASS: **12561**
- REVIEW: **2759**
- FAIL: **1290**
- Eligible HLS at least 1080 lines before deduplication: **4788**
- Unique channels selected: **3623**
- STB-safe channels without special HTTP headers: **3366**

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
| Auto | 7 |
| Business | 23 |
| Classic | 8 |
| Comedy | 17 |
| Cooking | 13 |
| Culture | 34 |
| Documentary | 73 |
| Education | 55 |
| Entertainment | 189 |
| Family | 16 |
| General | 765 |
| Kids | 75 |
| Legislative | 38 |
| Lifestyle | 37 |
| Movies | 145 |
| Music | 272 |
| News | 331 |
| Outdoor | 27 |
| Public | 1 |
| Relax | 2 |
| Religious | 224 |
| Science | 7 |
| Series | 63 |
| Shop | 16 |
| Sports | 157 |
| Travel | 15 |
| Unclassified | 997 |
| Weather | 5 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
