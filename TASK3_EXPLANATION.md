# Task 3: Perbedaan Pendekatan File Kecil vs File Besar

## Strategi Loading

File kecil (`customers-100000.csv`, 17MB) diproses dengan `pd.read_csv()`
biasa, yaitu pendekatan **eager loading**: seluruh isi file langsung
dibaca dan disimpan sebagai satu DataFrame utuh di memory. Pendekatan
ini aman karena ukurannya jauh di bawah kapasitas RAM laptop pada
umumnya.

File besar (`customers-2000000.csv`, 336MB, 2 juta baris) diproses
dengan `csv.DictReader()`, yaitu pendekatan **streaming**: baris dibaca
dan diproses satu per satu, lalu langsung dibuang dari memory setelah
selesai. Yang disimpan hanya hasil agregasi (running counter), bukan
datanya sendiri.

## Mengapa Pendekatan Perlu Berbeda

Ukuran file di disk tidak mencerminkan ukurannya di memory. Pada
pengujian ini, file 336MB yang dimuat penuh melalui pandas memakan
**1.156 MB RAM**, sekitar 3,4 kali lipat dari ukuran aslinya. Hal ini
terjadi akibat overhead pandas untuk tipe data, index, dan representasi
objek per kolom. Memory ini bertumbuh linear seiring ukuran file,
sehingga untuk dataset yang jauh lebih besar, pendekatan ini dapat
dengan cepat menghabiskan RAM yang tersedia.

Pendekatan streaming tidak memiliki masalah ini: penggunaan memory
tetap konstan (~11 MB pada pengujian ini) berapa pun jumlah barisnya,
karena yang disimpan hanyalah state agregat, bukan data mentah.

## Trade-off

Pendekatan eager (pandas) lebih cepat karena operasinya vectorized dan
berjalan di level C, serta mendukung operasi kompleks lintas seluruh
data seperti join, sort, atau groupby. Namun, penggunaan memory-nya
proporsional terhadap ukuran data, sehingga cocok digunakan apabila
data dapat dimuat dengan nyaman di RAM.

Pendekatan streaming (csv module) sedikit lebih lambat karena diproses
baris demi baris di level Python, dan hanya cocok untuk operasi yang
dapat dihitung secara berjalan seperti running total atau counter.
Namun, penggunaan memory-nya konstan, sehingga menjadi satu-satunya
opsi yang feasible untuk data yang terlalu besar bagi RAM.

## Middle Ground: Chunking

Terdapat opsi tengah, `pd.read_csv(file, chunksize=100000)`, yang
membaca file per potongan (chunk) sebagai DataFrame kecil, memprosesnya,
lalu membuangnya sebelum melanjutkan ke chunk berikutnya. Pendekatan ini
menggabungkan kelebihan keduanya: tetap dapat memakai operasi vectorized
pandas per chunk, namun memory tetap terkendali karena tidak
proporsional terhadap ukuran keseluruhan file.
