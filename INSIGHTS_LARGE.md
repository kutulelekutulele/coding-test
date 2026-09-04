# Task 2: Low-Memory Parsing - customers-2000000.csv

## Perbandingan Pendekatan
| Metode | Peak Memory | Waktu |
|---|---|---|
| Naive (`pd.read_csv`, load semua) | 1,156.50 MB | 5.90 detik |
| Streaming (`csv.DictReader`, baris per baris) | 10.91 MB | 6.77 detik |

Pendekatan streaming mengurangi memory usage ~106x lipat, dengan trade-off
waktu proses sedikit lebih lambat (~0.9 detik). Untuk file yang jauh lebih
besar dari 2 juta baris, pendekatan streaming adalah satu-satunya opsi yang
feasible karena memory usage-nya konstan (tidak bertambah seiring ukuran file).

## Insight dari Data (2,000,000 baris)
- 243 negara unik
- Top negara: Korea (16,240), Congo (16,208) - polanya konsisten dengan
  dataset 100,000 baris, mengindikasikan data ini di-generate/fake.
