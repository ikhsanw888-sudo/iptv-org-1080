# iptv-org 1080 Scan Summary

- Streams tested: **16838**
- PASS: **12650**
- REVIEW: **2937**
- FAIL: **1248**
- Eligible HLS at least 1080 lines before deduplication: **4845**
- Unique channels selected: **3645**
- STB-safe channels without special HTTP headers: **3382**

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
| Auto | 5 |
| Business | 24 |
| Classic | 8 |
| Comedy | 16 |
| Cooking | 14 |
| Culture | 37 |
| Documentary | 72 |
| Education | 54 |
| Entertainment | 189 |
| Family | 16 |
| General | 768 |
| Kids | 83 |
| Legislative | 38 |
| Lifestyle | 35 |
| Movies | 141 |
| Music | 268 |
| News | 344 |
| Outdoor | 25 |
| Public | 1 |
| Relax | 2 |
| Religious | 232 |
| Science | 7 |
| Series | 66 |
| Shop | 17 |
| Sports | 162 |
| Travel | 16 |
| Unclassified | 988 |
| Weather | 6 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
