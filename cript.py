import string

# Fungsi ROT13
def rot13(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 13
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Fungsi brute force (coba semua shift)
def brute_force(text):
    alphabet = string.ascii_lowercase
    for shift in range(26):
        result = ""
        for char in text:
            if char.lower() in alphabet:
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        print(f"Shift {shift:2}: {result}")

# ===== MAIN PROGRAM =====
print("=== PROGRAM DEKRIPSI CIPHER ===")
cipher = input("Masukkan ciphertext: ")

print("\nHasil ROT13:")
print(rot13(cipher))

print("\nCoba semua kemungkinan shift (analisis frekuensi sederhana):")
brute_force(cipher)