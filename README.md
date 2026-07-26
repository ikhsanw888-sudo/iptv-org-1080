# iptv-org 1080 Workflow

Workflow ini mengambil data terbaru dari API resmi iptv-org, menguji semua URL
unik dengan `ffprobe`, memeriksa resolusi video aktual, menghapus duplikat, dan
membuat playlist 1080 yang dikelompokkan menurut genre.

## Hasil

- `generated/iptv-org-1080.m3u` — seluruh channel HLS 1080 terpilih
- `generated/iptv-org-1080-stb.m3u` — subset yang tidak memerlukan header HTTP khusus
- `generated/genres/*.m3u` — playlist terpisah per genre
- `reports/scan-summary.md` — ringkasan pengujian
- `reports/selected-1080.csv` — daftar channel yang terpilih
- Artifact `iptv-org-1080-output` — termasuk laporan lengkap terkompresi

## Aturan seleksi

Channel masuk playlist hanya ketika:

1. `ffprobe` menemukan video yang dapat diputar.
2. Tinggi video aktual minimal 1080 piksel.
3. Stream merupakan HLS/M3U8.
4. Channel tidak berstatus NSFW, tutup, atau masuk blocklist.
5. Stream menjadi pilihan terbaik setelah penghapusan URL dan channel duplikat.

Jika satu channel memiliki beberapa URL, pemilihan mempertimbangkan resolusi,
progressive/interlaced, main feed, label pembatasan, kebutuhan header khusus,
HTTPS, dan kecepatan respons.

## Menjalankan

Buka **Actions → Scan iptv-org and build 1080 playlists → Run workflow**.

Workflow juga berjalan otomatis setiap Minggu pukul 09.00 WIB.

## Catatan

- Stream yang dibatasi secara geografis dapat gagal dari server GitHub meskipun
  mungkin bekerja dari Indonesia.
- Workflow ini sebaiknya digunakan di repository terpisah agar tidak menimpa
  playlist 50 channel yang telah dikurasi.
- Pemindaian dijadwalkan mingguan, bukan harian, agar tidak membebani server
  broadcaster secara berlebihan.
