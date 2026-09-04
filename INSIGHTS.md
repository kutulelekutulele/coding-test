# Insight: customers-100000.csv

## Struktur Data
Terdapat 100.000 baris dan 12 kolom pada dataset ini, tanpa missing value
di kolom manapun. Kolom Customer Id bersifat unique (tidak ada duplikat),
sehingga valid dijadikan primary key.

## Data Quality Issue
Terdapat 5 pasang email duplikat (10 baris total), masing-masing dengan
Customer Id, nama depan, dan nama belakang yang berbeda. Kemungkinan besar
hal ini merupakan collision dari proses generate data (fake data), bukan
representasi pengguna yang benar-benar mendaftar dua kali.

## Distribusi Negara
Distribusi customer per negara tidak merata: Congo (835) dan Korea (820)
memiliki jumlah customer tertinggi, jauh di atas rata-rata negara lain.
Pola ini mengindikasikan data bersifat sintetis/generated, bukan
distribusi populasi customer riil.

## Company
Sebanyak 71.994 dari 100.000 baris memiliki company yang unik (sekitar
72%), yang menunjukkan bahwa kolom Company tidak merepresentasikan
pengelompokan customer secara realistis. Pada data riil, customer
umumnya lebih terkonsentrasi pada sejumlah perusahaan besar.

## Tren Subscription
Rentang tanggal subscription adalah 2020-01-01 sampai 2022-05-29, dengan
jumlah subscription per tahun sebagai berikut: 2020 (41.898), 2021
(41.211), dan 2022 (16.891). Angka tahun 2022 tidak dapat dibandingkan
secara langsung dengan tahun lainnya karena data yang tersedia hanya
mencakup sekitar lima bulan pertama, bukan satu tahun penuh.
