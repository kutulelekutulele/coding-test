import os
from datetime import date
from dotenv import load_dotenv
from google import genai
from google.genai import types

from db import get_items_by_date, get_total_by_date, get_merchants_by_item_and_daterange

load_dotenv()  # baca GEMINI_API_KEY dari file .env

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def get_food_by_date(date: str) -> str:
    """Mendapatkan daftar makanan/item yang dibeli pada tanggal tertentu.

    Args:
        date: Tanggal dalam format YYYY-MM-DD.
    """
    items = get_items_by_date(date)
    if not items:
        return f"Tidak ada data pembelian pada tanggal {date}."
    lines = [f"- {i['item_name']} (Rp{i['price']:,}) dari {i['merchant']}" for i in items]
    return "\n".join(lines)


def get_total_expense_by_date(date: str) -> str:
    """Mendapatkan total pengeluaran makanan pada tanggal tertentu.

    Args:
        date: Tanggal dalam format YYYY-MM-DD.
    """
    total = get_total_by_date(date)
    return f"Total pengeluaran pada {date}: Rp{total:,}"


def find_merchant_by_item(item_keyword: str, start_date: str, end_date: str) -> str:
    """Mencari toko/merchant tempat membeli item tertentu dalam rentang tanggal.

    Args:
        item_keyword: Kata kunci nama item yang dicari, misal 'hamburger'.
        start_date: Tanggal awal rentang pencarian, format YYYY-MM-DD.
        end_date: Tanggal akhir rentang pencarian, format YYYY-MM-DD.
    """
    results = get_merchants_by_item_and_daterange(item_keyword, start_date, end_date)
    if not results:
        return f"Tidak ditemukan pembelian '{item_keyword}' antara {start_date} dan {end_date}."
    lines = [f"- {r['merchant']} pada {r['purchase_date']}" for r in results]
    return "\n".join(lines)


def ask(question: str) -> str:
    today = date.today().isoformat()
    prompt = f"""Hari ini adalah tanggal {today}. Kamu adalah asisten yang membantu
user melacak riwayat pembelian makanan mereka. Jawab pertanyaan user menggunakan
tools yang tersedia. Hitung tanggal relatif (kemarin, minggu lalu, dst) berdasarkan
tanggal hari ini di atas. Jawab dalam Bahasa Indonesia yang natural.

Pertanyaan user: {question}"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[get_food_by_date, get_total_expense_by_date, find_merchant_by_item]
        ),
    )
    return response.text


if __name__ == "__main__":
    print("=== Test 1: Kemarin ===")
    print(ask("Makanan apa yang aku beli kemarin?"))

    print("\n=== Test 2: Total expense tanggal tertentu ===")
    print(ask("Berapa total pengeluaran makanan tanggal 20 Juni?"))

    print("\n=== Test 3: Cari merchant ===")
    print(ask("Di mana aku beli hamburger dalam 7 hari terakhir?"))
