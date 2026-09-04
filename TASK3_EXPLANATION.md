# Task 3: Perbedaan Pendekatan File Kecil vs File Besar

## Strategi Loading

File kecil (`customers-100000.csv`, 17MB) diproses dengan `pd.read_csv()` biasa — **eager loading**, seluruh isi file langsung dibaca dan disimpan sebagai satu DataFrame utuh di memory. Pendekatan ini aman karena ukurannya jauh di bawah kapasitas RAM laptop pada umumnya.

File besar (`customers-2000000.csv`, 336MB, 2 juta baris) diproses dengan `csv.DictReader()` — **streaming**, baris dibaca dan diproses satu per satu, lalu langsung dibuang dari memory setelah selesai. Yang disimpan hanya hasil agregasi (running counter), bukan datanya sendiri.

## Kenapa Perlu Beda

Ukuran file di disk tidak mencerminkan ukurannya di memory. Pada eksperimen saya, file 336MB yang di-load penuh lewat pandas memakan **1,156 MB RAM** — sekitar 3,4x lipat dari ukuran aslinya, akibat overhead pandas untuk tipe data, index, dan representasi objek per kolom. Memory ini bertumbuh linear seiring ukuran file, sehingga untuk dataset yang jauh lebih besar, pendekatan ini bisa dengan cepat menghabiskan RAM yang tersedia.

Pendekatan streaming tidak punya masalah ini: memory usage tetap konstan (~11 MB pada eksperimen saya) berapa pun jumlah barisnya, karena yang disimpan hanyalah state agregat, bukan data mentah.

## Trade-off

Pendekatan eager (pandas) lebih cepat karena operasinya vectorized dan berjalan di level C, serta mendukung operasi kompleks lintas seluruh data seperti join, sort, atau groupby — tapi memory usage-nya proporsional terhadap ukuran data, jadi cocok dipakai kalau datanya muat nyaman di RAM.

Pendekatan streaming (csv module) sedikit lebih lambat karena diproses baris demi baris di level Python, dan hanya cocok untuk operasi yang bisa dihitung secara berjalan seperti running total atau counter — tapi memory usage-nya konstan, sehingga jadi satu-satunya opsi yang feasible untuk data yang terlalu besar untuk RAM.

## Middle Ground: Chunking

Ada opsi tengah, `pd.read_csv(file, chunksize=100000)`, yang membaca file per potongan (chunk) sebagai DataFrame kecil, memprosesnya, lalu membuangnya sebelum lanjut ke chunk berikutnya. Ini menggabungkan kelebihan keduanya — masih bisa memakai operasi vectorized pandas per chunk, namun memory tetap terkendali karena tidak proporsional terhadap ukuran keseluruhan file.
