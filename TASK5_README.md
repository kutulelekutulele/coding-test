# Task 5: Receipt Tracker Platform

## Arsitektur
- **Backend**: Flask (`app.py`)
- **OCR**: Tesseract via pytesseract (`parse_receipt.py`)
- **Database**: SQLite (`db.py`)
- **AI Tools**: Gemini API function calling (`llm_tools.py`)
- **UI**: HTML + vanilla JS (`templates/index.html`)

## Fitur
- **Upload struk** (`/upload`): user upload foto struk + input manual nama toko
  & tanggal (manual, bukan auto-extract, karena OCR pada foto asli terbukti
  kurang akurat - lihat catatan di bawah). OCR mengekstrak nama item & harga,
  disimpan ke SQLite.
- **Tanya AI** (`/ask`): user tanya pertanyaan natural language, Gemini
  memutuskan tool mana yang dipanggil (get_food_by_date, get_total_expense_by_date,
  find_merchant_by_item), lalu menyusun jawaban dari hasil query database.

## Cara Menjalankan
```bash
pip install -r requirements.txt
brew install tesseract
# isi .env dengan GEMINI_API_KEY=...
python3 app.py
```
Buka `http://127.0.0.1:5002`

## Catatan & Limitasi
- Akurasi OCR sangat dipengaruhi kualitas foto (pencahayaan, glare, sudut).
  Pada foto struk asli dengan glare, hanya 1 dari 8 item berhasil terbaca
  dengan benar. Nama toko & tanggal diminta manual untuk menjaga akurasi
  data yang dipakai untuk query (lebih krusial dari nama item).
- Parsing menggunakan regex sederhana (cari baris dengan pola angka format
  ribuan). Tidak menangani item yang nama-nya terpotong jadi multi-baris.
- Search vector DB (Task 4) belum diintegrasikan ke sini - masih berdiri
  sendiri sebagai service terpisah.
