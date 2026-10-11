# iptv-org 1080 Scan Summary

- Streams tested: **17954**
- PASS: **10734**
- REVIEW: **5601**
- FAIL: **1614**
- Eligible HLS at least 1080 lines before deduplication: **4765**
- Unique channels selected: **3642**
- STB-safe channels without special HTTP headers: **3388**

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
| Auto | 8 |
| Business | 26 |
| Classic | 8 |
| Comedy | 17 |
| Cooking | 16 |
| Culture | 44 |
| Documentary | 78 |
| Education | 54 |
| Entertainment | 198 |
| Family | 16 |
| General | 715 |
| Kids | 75 |
| Legislative | 31 |
| Lifestyle | 41 |
| Movies | 172 |
| Music | 276 |
| News | 362 |
| Outdoor | 28 |
| Public | 1 |
| Relax | 2 |
| Religious | 238 |
| Science | 7 |
| Series | 71 |
| Shop | 15 |
| Sports | 174 |
| Travel | 19 |
| Unclassified | 933 |
| Weather | 6 |

> A GitHub-hosted runner may be blocked by geo-restricted streams that could still work from Indonesia. REVIEW items remain in the full report but are not included in generated playlists.
