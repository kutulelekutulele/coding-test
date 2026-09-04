import pytesseract
from PIL import Image

img = Image.open("sample_receipt.jpeg")
text = pytesseract.image_to_string(img)

print("=== HASIL OCR MENTAH ===")
print(text)
