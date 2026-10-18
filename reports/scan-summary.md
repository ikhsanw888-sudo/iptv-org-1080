# iptv-org 1080 Scan Summary

- Streams tested: **18109**
- PASS: **12828**
- REVIEW: **3629**
- FAIL: **1647**
- Eligible HLS at least 1080 lines before deduplication: **4865**
- Unique channels selected: **3726**
- STB-safe channels without special HTTP headers: **3471**

## Outputs

- `generated/iptv-org-1080.m3u`: all selected 1080 HLS channels
- `generated/iptv-org-1080-stb.m3u`: safer subset for older STBs
- `generated/genres/*.m3u`: one playlist per genre
- `reports/selected-1080.csv`: selected-channel audit table
- `reports/all-results.csv.gz`: complete scan report (workflow artifact)

## Channels by genre

| Genre | Channels |
|---|---:|
| Animation | 10 |
| Auto | 10 |
| Business | 29 |
| Classic | 9 |
| Comedy | 18 |
| Cooking | 19 |
| Culture | 44 |
| Documentary | 85 |
| Education | 52 |
| Entertainment | 200 |
| Family | 19 |
| General | 718 |
| Kids | 85 |
| Legislative | 32 |
| Lifestyle | 45 |
| Movies | 176 |
| Music | 276 |
| News | 375 |
| Outdoor | 26 |
| Public | 1 |
| Relax | 2 |
| Religious | 241 |
| Science | 8 |
| Series | 73 |
| Shop | 17 |
| Sports | 175 |
| Travel | 20 |
| Unclassified | 955 |
| Weather | 6 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
