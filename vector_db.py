import json
from vector_math import cosine_similarity

class VectorDB:
    def __init__(self):
        self.records = {}  # id -> {"vector": [...], "metadata": {...}}

    def add(self, id, vector, metadata=None):
        self.records[id] = {
            "vector": vector,
            "metadata": metadata or {}
        }

    def search(self, query_vector, top_k=5):
        scored = []
        for id, record in self.records.items():
            score = cosine_similarity(query_vector, record["vector"])
            scored.append((id, score, record["metadata"]))

        # urutkan dari similarity tertinggi ke terendah
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def save(self, filepath):
        """Simpan seluruh data ke file JSON, biar persist (nggak hilang tiap restart)."""
        with open(filepath, "w") as f:
            json.dump(self.records, f)

    def load(self, filepath):
        """Baca kembali data dari file JSON."""
        with open(filepath, "r") as f:
            self.records = json.load(f)
