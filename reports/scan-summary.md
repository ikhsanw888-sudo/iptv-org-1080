# iptv-org 1080 Scan Summary

- Streams tested: **18637**
- PASS: **12753**
- REVIEW: **3748**
- FAIL: **2131**
- Eligible HLS at least 1080 lines before deduplication: **4555**
- Unique channels selected: **3608**
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
| Animation | 10 |
| Auto | 9 |
| Business | 26 |
| Classic | 7 |
| Comedy | 17 |
| Cooking | 16 |
| Culture | 38 |
| Documentary | 77 |
| Education | 47 |
| Entertainment | 203 |
| Family | 16 |
| General | 701 |
| Kids | 87 |
| Legislative | 32 |
| Lifestyle | 40 |
| Movies | 173 |
| Music | 298 |
| News | 368 |
| Outdoor | 26 |
| Public | 1 |
| Relax | 1 |
| Religious | 251 |
| Science | 7 |
| Series | 72 |
| Shop | 16 |
| Sports | 165 |
| Travel | 23 |
| Unclassified | 876 |
| Weather | 5 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
