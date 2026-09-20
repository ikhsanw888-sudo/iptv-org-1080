# iptv-org 1080 Scan Summary

- Streams tested: **17564**
- PASS: **12627**
- REVIEW: **3355**
- FAIL: **1579**
- Eligible HLS at least 1080 lines before deduplication: **4743**
- Unique channels selected: **3567**
- STB-safe channels without special HTTP headers: **3320**

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
| Auto | 8 |
| Business | 27 |
| Classic | 8 |
| Comedy | 17 |
| Cooking | 13 |
| Culture | 40 |
| Documentary | 78 |
| Education | 52 |
| Entertainment | 186 |
| Family | 12 |
| General | 711 |
| Kids | 78 |
| Legislative | 31 |
| Lifestyle | 38 |
| Movies | 169 |
| Music | 272 |
| News | 351 |
| Outdoor | 24 |
| Public | 1 |
| Relax | 2 |
| Religious | 237 |
| Science | 8 |
| Series | 68 |
| Shop | 17 |
| Sports | 153 |
| Travel | 20 |
| Unclassified | 929 |
| Weather | 5 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
