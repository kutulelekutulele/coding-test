FROM python:3.12-slim

# Install Tesseract OCR (dependency sistem, bukan Python package)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy & install dependency Python dulu (biar layer ini di-cache,
# nggak perlu install ulang tiap kali cuma kode app yang berubah)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code aplikasi (cuma yang dibutuhin app Task 5)
COPY app.py db.py parse_receipt.py llm_tools.py ./
COPY templates/ templates/

RUN mkdir -p uploads

EXPOSE 5002

CMD ["python3", "app.py"]
