# iptv-org 1080 Scan Summary

- Streams tested: **18689**
- PASS: **12754**
- REVIEW: **3809**
- FAIL: **2121**
- Eligible HLS at least 1080 lines before deduplication: **4604**
- Unique channels selected: **3640**
- STB-safe channels without special HTTP headers: **3375**

## Outputs

- `generated/iptv-org-1080.m3u`: all selected 1080 HLS channels
- `generated/iptv-org-1080-stb.m3u`: safer subset for older STBs
- `generated/genres/*.m3u`: one playlist per genre
- `reports/selected-1080.csv`: selected-channel audit table
- `reports/all-results.csv.gz`: complete scan report (workflow artifact)

## Channels by genre

| Genre | Channels |
|---|---:|
| Animation | 9 |
| Auto | 9 |
| Business | 26 |
| Classic | 8 |
| Comedy | 16 |
| Cooking | 16 |
| Culture | 43 |
| Documentary | 78 |
| Education | 49 |
| Entertainment | 205 |
| Family | 15 |
| General | 713 |
| Kids | 86 |
| Legislative | 32 |
| Lifestyle | 41 |
| Movies | 163 |
| Music | 288 |
| News | 395 |
| Outdoor | 26 |
| Public | 1 |
| Relax | 1 |
| Religious | 248 |
| Science | 7 |
| Series | 72 |
| Shop | 18 |
| Sports | 173 |
| Travel | 23 |
| Unclassified | 873 |
| Weather | 6 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
