# iptv-org 1080 Scan Summary

- Streams tested: **17842**
- PASS: **12968**
- REVIEW: **3104**
- FAIL: **1768**
- Eligible HLS at least 1080 lines before deduplication: **5002**
- Unique channels selected: **3726**
- STB-safe channels without special HTTP headers: **3493**

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
| Business | 26 |
| Classic | 8 |
| Comedy | 18 |
| Cooking | 12 |
| Culture | 39 |
| Documentary | 68 |
| Education | 57 |
| Entertainment | 201 |
| Family | 18 |
| General | 766 |
| Kids | 80 |
| Legislative | 44 |
| Lifestyle | 38 |
| Movies | 155 |
| Music | 275 |
| News | 332 |
| Outdoor | 27 |
| Public | 1 |
| Relax | 2 |
| Religious | 233 |
| Science | 8 |
| Series | 66 |
| Shop | 20 |
| Sports | 170 |
| Travel | 15 |
| Unclassified | 1024 |
| Weather | 6 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
