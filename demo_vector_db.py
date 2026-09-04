from vector_db import VectorDB

db = VectorDB()

# contoh data: representasi sederhana beberapa "makanan" dalam 3 dimensi
# (anggap aja 3 angka ini semacam skor: [manis, asin, pedas])
db.add("nasi_goreng", [2, 8, 6], {"name": "Nasi Goreng"})
db.add("es_teh", [9, 1, 0], {"name": "Es Teh"})
db.add("rendang", [3, 7, 8], {"name": "Rendang"})
db.add("kue_lapis", [9, 2, 0], {"name": "Kue Lapis"})
db.add("sate_padang", [2, 6, 9], {"name": "Sate Padang"})

# query: cari makanan yang mirip dengan sesuatu yang "asin & pedas" [1, 7, 8]
query = [1, 7, 8]
results = db.search(query, top_k=3)

print("Query: [asin & pedas tinggi]")
print("Hasil pencarian (paling mirip dulu):")
for id, score, metadata in results:
    print(f"  {metadata['name']} (id={id}) - similarity: {score:.4f}")

# test save & load
db.save("vector_db_data.json")
print("\nData tersimpan ke vector_db_data.json")
