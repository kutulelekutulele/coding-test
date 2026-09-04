import re

PRICE_PATTERN = re.compile(r'(\d{1,3}(?:,\d{3})+)')

def parse_receipt_text(raw_text):
    """
    Cari baris yang punya minimal 2 angka format ribuan (price & total).
    Nama item diambil dari teks sebelum angka pertama.
    """
    items = []
    lines = raw_text.split("\n")

    for line in lines:
        prices = PRICE_PATTERN.findall(line)
        if len(prices) >= 2:
            total = int(prices[-1].replace(",", ""))

            # ambil teks sebelum angka pertama sebagai nama item
            name_part = PRICE_PATTERN.split(line)[0]
            # buang karakter aneh hasil noise OCR, sisain huruf & spasi aja
            name = re.sub(r'[^a-zA-Z ]', '', name_part).strip()

            if name:
                items.append({"item_name": name, "price": total})

    return items


if __name__ == "__main__":
    import pytesseract
    from PIL import Image

    img = Image.open("sample_receipt.jpeg")
    raw_text = pytesseract.image_to_string(img)

    items = parse_receipt_text(raw_text)

    print("=== ITEM YANG BERHASIL DI-PARSE ===")
    for item in items:
        print(item)
