# Task 4: Vector DB dari Scratch

## Implementasi
- `vector_math.py` - implementasi cosine similarity manual (dot product,
  magnitude) tanpa numpy/scikit-learn, murni pakai loop Python + math.sqrt.
- `vector_db.py` - class VectorDB sederhana (brute-force linear scan),
  mendukung add, search (top-k by cosine similarity), save/load ke JSON.
- `vector_db_api.py` - membungkus VectorDB jadi HTTP API pakai Flask,
  sehingga "di-deploy" sebagai service sendiri (self-hosted), bukan
  memakai layanan vector DB terkelola (Pinecone/Weaviate/dst).

## Cara Menjalankan
```bash
pip install -r requirements.txt
python3 vector_db_api.py
```
Server jalan di `http://127.0.0.1:5001`.

## Endpoint
- `GET /health` - cek status server
- `POST /add` - body: `{"id": "...", "vector": [...], "metadata": {...}}`
- `POST /search` - body: `{"vector": [...], "top_k": 5}`

## Catatan
Search menggunakan brute-force (bandingkan ke semua record). Untuk dataset
besar (jutaan vector), production vector DB biasanya pakai algoritma index
approximate nearest neighbor (HNSW, IVF) supaya tidak perlu scan semua data.
