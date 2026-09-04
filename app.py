from flask import Flask, request, jsonify, render_template
import os
from PIL import Image
import pytesseract

from parse_receipt import parse_receipt_text
from db import init_db, insert_item

app = Flask(__name__)
init_db()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "File tidak ditemukan"}), 400

    file = request.files["file"]
    merchant = request.form.get("merchant", "Unknown")
    purchase_date = request.form.get("purchase_date")

    if not purchase_date:
        return jsonify({"error": "Tanggal wajib diisi"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    img = Image.open(filepath)
    raw_text = pytesseract.image_to_string(img)
    items = parse_receipt_text(raw_text)

    for item in items:
        insert_item(merchant, purchase_date, item["item_name"], item["price"])

    return jsonify({
        "status": "ok",
        "merchant": merchant,
        "purchase_date": purchase_date,
        "items_saved": len(items),
        "items": items
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
