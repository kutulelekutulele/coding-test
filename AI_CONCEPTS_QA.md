# Pertanyaan Konsep AI

## 1. Perbedaan REST API dan MCP dalam Konteks AI

REST API adalah standar komunikasi antar sistem melalui HTTP dengan endpoint
yang sudah ditentukan lebih dulu. Developer perlu memahami skema tiap API
secara manual dari dokumentasi, lalu mengintegrasikannya satu per satu ke
dalam kode.

MCP (Model Context Protocol) dirancang khusus untuk kebutuhan AI agent.
Tools dan data yang diekspos melalui MCP server memiliki skema yang dapat
dibaca dan dipahami langsung oleh LLM, sehingga agent dapat mengenali
kapabilitas yang tersedia secara dinamis tanpa perlu integrasi manual untuk
setiap API baru.

## 2. Bagaimana REST API dan MCP Meningkatkan Use Case AI

REST API memungkinkan AI agent mengakses data di luar pengetahuan hasil
training, misalnya data internal perusahaan atau harga saham terkini, serta
menjalankan aksi nyata seperti membuat order, bukan sekadar menghasilkan
teks.

MCP membuat integrasi tools menjadi reusable. Satu MCP server dapat
digunakan oleh banyak AI client tanpa perlu menulis ulang integrasi khusus
untuk masing-masing client, sehingga ekosistem tools untuk AI agent menjadi
lebih scalable. Pada Task 5 proyek ini, prinsip serupa diterapkan melalui
function calling, di mana Gemini memanggil fungsi database secara langsung
berdasarkan pertanyaan pengguna, bukan melalui endpoint REST statis yang
logikanya sudah di-hardcode.

## 3. Cara Memastikan AI Agent Menjawab dengan Benar

Beberapa pendekatan yang umum digunakan:

Jawaban di-ground pada data nyata melalui function calling ke database atau
API, bukan hanya mengandalkan pengetahuan internal model. Pengujian
dilakukan dengan kasus yang jawabannya sudah diketahui, termasuk kasus data
kosong, seperti query tanggal tanpa transaksi pada Task 5 yang seharusnya
dijawab Rp0, bukan dikarang. Eval set berupa kumpulan pertanyaan dan jawaban
benar disiapkan untuk mengecek regresi setiap ada perubahan pada sistem.
Model juga diberi instruksi eksplisit untuk menyatakan "tidak ditemukan"
apabila data memang tidak tersedia, alih-alih menebak.

## 4. Docker dan Containerized Environment dalam Konteks AI

Docker memastikan environment aplikasi AI (versi Python, library, dependency
sistem seperti Tesseract OCR) konsisten di semua tempat aplikasi dijalankan,
sehingga masalah "jalan di laptop saya tapi tidak jalan di server" dapat
dihindari.

Container juga memudahkan deployment dan scaling. Aplikasi yang sudah
di-containerize dapat dijalankan di berbagai platform cloud tanpa
konfigurasi ulang, dan dapat di-scale dengan menjalankan banyak instance
container sesuai kebutuhan. Selain itu, containerization mempermudah proses
CI/CD karena build dan test dapat dijalankan pada environment yang identik
dengan environment produksi. Pada Task 6 proyek ini, Dockerfile digunakan
untuk membungkus aplikasi beserta dependency-nya, dan GitHub Actions
menjalankan build serta smoke test otomatis di dalam container tersebut.

## 5. Cara Fine-Tune LLM Model dari Raw

Proses fine-tuning dari model dasar (base/raw model) umumnya mencakup
beberapa tahap berikut.

Dataset disiapkan dalam format instruksi-respons yang relevan dengan use
case, kemudian dibersihkan dari data yang tidak konsisten atau berkualitas
rendah. Base model dipilih sesuai kebutuhan (ukuran, lisensi, kapabilitas
dasar), lalu proses training dijalankan dengan menyesuaikan bobot model
menggunakan dataset tersebut, biasanya dengan teknik seperti LoRA atau
QLoRA agar kebutuhan resource lebih efisien dibanding full fine-tuning.
Hyperparameter seperti learning rate dan jumlah epoch disesuaikan agar
model tidak overfitting terhadap dataset training. Setelah training
selesai, model dievaluasi menggunakan data yang belum pernah dilihat
sebelumnya untuk memastikan performa dan menghindari catastrophic
forgetting terhadap kemampuan umum model. Model yang sudah lolos evaluasi
kemudian di-deploy dan dipantau performanya di production.
