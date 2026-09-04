import pandas as pd
import time
import resource
import sys

start_time = time.time()

df = pd.read_csv("customers-2000000.csv")

elapsed = time.time() - start_time

# ru_maxrss satuannya beda per OS: macOS = bytes, Linux = kilobytes
peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
peak_mb = peak / (1024 * 1024) if sys.platform == "darwin" else peak / 1024

print(f"Jumlah baris: {len(df)}")
print(f"Waktu load: {elapsed:.2f} detik")
print(f"Peak memory usage: {peak_mb:.2f} MB")
