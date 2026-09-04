import pandas as pd

# baca CSV jadi DataFrame (tabel di memory)
df = pd.read_csv("customers-100000.csv")

# (baris, kolom) -> ukuran datanya
print("Shape:", df.shape)
print()

# tipe data tiap kolom + berapa banyak non-null value
print("Info:")
df.info()
print()

# lihat 5 baris pertama, buat sanity check datanya
print("Head:")
print(df.head())
print()

# hitung berapa banyak missing value per kolom
print("Missing values per column:")
print(df.isnull().sum())
print()

# --- Insight 1: Top 10 negara dengan customer terbanyak ---
print("Top 10 Countries:")
print(df["Country"].value_counts().head(10))
print()

# --- Insight 2: Berapa banyak company yang unik ---
print("Jumlah unique companies:", df["Company"].nunique())
print()

# --- Insight 3: Cek data quality - ada duplikat Customer Id / Email? ---
print("Jumlah Customer Id duplikat:", df["Customer Id"].duplicated().sum())
print("Jumlah Email duplikat:", df["Email"].duplicated().sum())
# --- Investigasi: baris mana aja yang emailnya duplikat ---
print("Detail baris dengan email duplikat:")
dup_emails = df[df["Email"].duplicated(keep=False)]
print(dup_emails[["Customer Id", "First Name", "Last Name", "Email"]].sort_values("Email"))

# --- Insight 4: Trend subscription dari waktu ke waktu ---
df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])

print("Rentang tanggal subscription:", df["Subscription Date"].min(), "-", df["Subscription Date"].max())
print()

print("Jumlah subscription per tahun:")
print(df["Subscription Date"].dt.year.value_counts().sort_index())
