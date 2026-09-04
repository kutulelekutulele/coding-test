from flask import Flask, request, jsonify
from vector_db import VectorDB
import os

app = Flask(__name__)
db = VectorDB()

DATA_FILE = "vector_db_data.json"

# load data yang udah ada (kalau file-nya udah pernah disimpan sebelumnya)
if os.path.exists(DATA_FILE):
    db.load(DATA_FILE)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "total_records": len(db.records)})

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    id = data.get("id")
    vector = data.get("vector")
    metadata = data.get("metadata", {})

    if not id or not vector:
        return jsonify({"error": "id dan vector wajib diisi"}), 400

    db.add(id, vector, metadata)
    db.save(DATA_FILE)  # persist tiap kali ada penambahan

    return jsonify({"status": "added", "id": id}), 201

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query_vector = data.get("vector")
    top_k = data.get("top_k", 5)

    if not query_vector:
        return jsonify({"error": "vector wajib diisi"}), 400

    results = db.search(query_vector, top_k=top_k)
    formatted = [
        {"id": id, "similarity": score, "metadata": metadata}
        for id, score, metadata in results
    ]
    return jsonify({"results": formatted})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
