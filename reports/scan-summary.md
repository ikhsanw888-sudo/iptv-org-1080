# iptv-org 1080 Scan Summary

- Streams tested: **17214**
- PASS: **12249**
- REVIEW: **3367**
- FAIL: **1595**
- Eligible HLS at least 1080 lines before deduplication: **4660**
- Unique channels selected: **3538**
- STB-safe channels without special HTTP headers: **3277**

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
| Business | 24 |
| Classic | 7 |
| Comedy | 18 |
| Cooking | 11 |
| Culture | 42 |
| Documentary | 75 |
| Education | 56 |
| Entertainment | 194 |
| Family | 14 |
| General | 722 |
| Kids | 83 |
| Legislative | 36 |
| Lifestyle | 37 |
| Movies | 165 |
| Music | 263 |
| News | 326 |
| Outdoor | 23 |
| Public | 1 |
| Relax | 2 |
| Religious | 221 |
| Science | 7 |
| Series | 67 |
| Shop | 18 |
| Sports | 151 |
| Travel | 18 |
| Unclassified | 934 |
| Weather | 5 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
