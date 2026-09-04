# Task 2: Low-Memory Parsing - customers-2000000.csv

## Perbandingan Pendekatan
Pada eksperimen ini, pendekatan naive (`pd.read_csv`, memuat seluruh data
sekaligus) memakan peak memory sebesar 1.156,50 MB dalam waktu 5,90 detik.
Pendekatan streaming (`csv.DictReader`, membaca baris per baris) hanya
memakan 10,91 MB dengan waktu 6,77 detik.

Pendekatan streaming mengurangi penggunaan memory sekitar 106 kali lipat,
dengan trade-off waktu proses yang sedikit lebih lambat (sekitar 0,9
detik). Untuk file yang jauh lebih besar dari 2 juta baris, pendekatan
streaming menjadi satu-satunya opsi yang feasible karena penggunaan
memory-nya konstan dan tidak bertambah seiring ukuran file.

## Insight dari Data (2.000.000 baris)
Terdapat 243 negara unik pada dataset ini. Negara dengan jumlah customer
tertinggi adalah Korea (16.240) dan Congo (16.208). Pola ini konsisten
dengan dataset 100.000 baris, yang mengindikasikan bahwa data ini bersifat
generated/fake.
