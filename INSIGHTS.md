# Insight: customers-100000.csv

## Struktur Data
- 100,000 baris, 12 kolom
- Tidak ada missing value di kolom manapun
- `Customer Id` bersifat unique (0 duplikat) → valid sebagai primary key

## Data Quality Issue
- Ditemukan 5 pasang email duplikat (10 baris total), masing-masing dengan
  Customer Id, nama depan, dan nama belakang yang berbeda. Kemungkinan besar
  ini adalah collision dari proses generate data (fake data), bukan
  representasi user yang mendaftar dua kali.

## Distribusi Negara
- Distribusi customer per negara tidak merata: Congo (835) dan Korea (820)
  memiliki jumlah customer tertinggi, jauh di atas rata-rata negara lain.
  Pola ini mengindikasikan data sintetis/generated, bukan distribusi
  populasi customer riil.

## Company
- 71,994 dari 100,000 baris memiliki company yang unik (~72%), menunjukkan
  kolom Company tidak merepresentasikan pengelompokan customer yang
  realistis (di data riil biasanya lebih terkonsentrasi ke beberapa
  perusahaan besar).

## Tren Subscription
- Rentang tanggal subscription: 2020-01-01 s/d 2022-05-29
- Jumlah subscription per tahun: 2020 (41,898), 2021 (41,211), 2022 (16,891)
- Catatan: angka 2022 tidak bisa dibandingkan langsung dengan 2020/2021
  karena datanya cuma mencakup ~5 bulan pertama 2022, bukan setahun penuh.
