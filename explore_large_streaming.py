import csv
import time
import resource
import sys

start_time = time.time()

country_counts = {}
row_count = 0

with open("customers-2000000.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row_count += 1
        country = row["Country"]
        country_counts[country] = country_counts.get(country, 0) + 1

elapsed = time.time() - start_time

peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
peak_mb = peak / (1024 * 1024) if sys.platform == "darwin" else peak / 1024

print(f"Jumlah baris: {row_count}")
print(f"Jumlah negara unik: {len(country_counts)}")
print(f"Waktu proses: {elapsed:.2f} detik")
print(f"Peak memory usage: {peak_mb:.2f} MB")

top10 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTop 10 Countries:")
for country, count in top10:
    print(f"{country}: {count}")
