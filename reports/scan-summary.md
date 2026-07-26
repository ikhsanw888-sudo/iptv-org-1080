# iptv-org 1080 Scan Summary

- Streams tested: **18143**
- PASS: **13176**
- REVIEW: **3239**
- FAIL: **1726**
- Eligible HLS at least 1080 lines before deduplication: **5074**
- Unique channels selected: **3771**
- STB-safe channels without special HTTP headers: **3475**

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
| Business | 25 |
| Classic | 8 |
| Comedy | 19 |
| Cooking | 13 |
| Culture | 37 |
| Documentary | 65 |
| Education | 55 |
| Entertainment | 203 |
| Family | 16 |
| General | 777 |
| Kids | 79 |
| Legislative | 44 |
| Lifestyle | 37 |
| Movies | 168 |
| Music | 283 |
| News | 339 |
| Outdoor | 26 |
| Public | 1 |
| Relax | 2 |
| Religious | 229 |
| Science | 7 |
| Series | 66 |
| Shop | 20 |
| Sports | 170 |
| Travel | 16 |
| Unclassified | 1040 |
| Weather | 8 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
