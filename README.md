# Coding Test - Ariadi Pradana

## Task 1-3: Data Exploration (customers CSV)
- `explore_small.py`, `INSIGHTS.md` - insight file kecil (100k baris)
- `explore_large_naive.py`, `explore_large_streaming.py`, `INSIGHTS_LARGE.md` - parsing file besar (2jt baris) low-memory
- `TASK3_EXPLANATION.md` - perbandingan pendekatan

## Task 4: Vector DB dari Scratch
- `vector_math.py`, `vector_db.py`, `vector_db_api.py`
- `TASK4_README.md` - dokumentasi & cara jalanin

## Task 5: Receipt Tracker Platform
- `app.py`, `db.py`, `parse_receipt.py`, `llm_tools.py`, `templates/`
- `TASK5_README.md` - dokumentasi & limitasi

## Task 6: Docker & CI/CD
- `Dockerfile`, `.dockerignore`, `.github/workflows/docker-build.yml`

## Note for Task 5
```bash
pip install -r requirements.txt
brew install tesseract
python3 app.py          # http://127.0.0.1:5002
```
Docker: `docker build -t receipt-tracker . && docker run -p 5002:5002 --env-file .env receipt-tracker`
