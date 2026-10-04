# iptv-org 1080 Scan Summary

- Streams tested: **18139**
- PASS: **12726**
- REVIEW: **3670**
- FAIL: **1739**
- Eligible HLS at least 1080 lines before deduplication: **4661**
- Unique channels selected: **3550**
- STB-safe channels without special HTTP headers: **3298**

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
| Business | 26 |
| Classic | 9 |
| Comedy | 18 |
| Cooking | 12 |
| Culture | 41 |
| Documentary | 69 |
| Education | 52 |
| Entertainment | 195 |
| Family | 13 |
| General | 694 |
| Kids | 78 |
| Legislative | 31 |
| Lifestyle | 38 |
| Movies | 169 |
| Music | 259 |
| News | 365 |
| Outdoor | 26 |
| Public | 1 |
| Relax | 2 |
| Religious | 239 |
| Science | 7 |
| Series | 69 |
| Shop | 16 |
| Sports | 151 |
| Travel | 19 |
| Unclassified | 928 |
| Weather | 5 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
