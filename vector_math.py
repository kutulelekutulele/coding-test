import math

def dot_product(a, b):
    """Jumlah dari perkalian elemen-elemen yang posisinya sama."""
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total

def magnitude(v):
    """Akar dari jumlah kuadrat semua elemen (panjang vector)."""
    sum_of_squares = 0
    for x in v:
        sum_of_squares += x ** 2
    return math.sqrt(sum_of_squares)

def cosine_similarity(a, b):
    """Ukur kemiripan 2 vector berdasarkan sudut di antaranya. Hasil: -1 s/d 1."""
    if len(a) != len(b):
        raise ValueError("Vector harus punya dimensi yang sama")

    dot = dot_product(a, b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)

    if mag_a == 0 or mag_b == 0:
        return 0.0  # hindari pembagian dengan nol

    return dot / (mag_a * mag_b)


# --- Test manual ---
if __name__ == "__main__":
    v1 = [1, 0, 0]
    v2 = [1, 0, 0]
    v3 = [0, 1, 0]
    v4 = [-1, 0, 0]

    print("v1 vs v2 (identik):", cosine_similarity(v1, v2))       # harus 1.0
    print("v1 vs v3 (tegak lurus):", cosine_similarity(v1, v3))   # harus 0.0
    print("v1 vs v4 (berlawanan):", cosine_similarity(v1, v4))    # harus -1.0
