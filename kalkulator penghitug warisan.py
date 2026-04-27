def hitung_waris():
    print("=== KALKULATOR WARIS ISLAM (LEBIH LENGKAP) ===")

    total = float(input("Total harta: "))

    # Pasangan
    suami = int(input("Suami (0/1): "))
    istri = int(input("Jumlah istri: "))

    # Orang tua
    ayah = int(input("Ayah (0/1): "))
    ibu = int(input("Ibu (0/1): "))

    # Kakek / Nenek
    kakek = int(input("Kakek (0/1): "))
    nenek = int(input("Nenek (0/1): "))

    # Anak
    anak_l = int(input("Anak laki-laki: "))
    anak_p = int(input("Anak perempuan: "))

    # Cucu dari anak laki-laki
    cucu_l = int(input("Cucu laki-laki (dari anak laki): "))
    cucu_p = int(input("Cucu perempuan (dari anak laki): "))

    # Saudara kandung
    saudara_l = int(input("Saudara laki-laki kandung: "))
    saudara_p = int(input("Saudara perempuan kandung: "))

    bagian = {}

    ada_anak = (anak_l + anak_p) > 0
    ada_cucu = (cucu_l + cucu_p) > 0

    # ======================
    # SUAMI / ISTRI
    # ======================
    if suami:
        bagian["Suami"] = total * (1/4 if ada_anak else 1/2)

    if istri > 0:
        bagian["Istri"] = total * (1/8 if ada_anak else 1/4)

    # ======================
    # IBU / NENEK
    # ======================
    if ibu:
        bagian["Ibu"] = total * (1/6 if ada_anak else 1/3)
    elif nenek:
        bagian["Nenek"] = total * (1/6)

    # ======================
    # AYAH / KAKEK
    # ======================
    if ayah:
        bagian["Ayah"] = total * (1/6 if ada_anak else 0)
    elif kakek:
        bagian["Kakek"] = total * (1/6 if ada_anak else 0)

    # ======================
    # HITUNG SISA
    # ======================
    terpakai = sum(bagian.values())
    sisa = total - terpakai

    # ======================
    # ANAK
    # ======================
    if ada_anak:
        unit = anak_l * 2 + anak_p
        if unit > 0:
            nilai = sisa / unit
            if anak_l:
                bagian["Anak Laki"] = nilai * 2 * anak_l
            if anak_p:
                bagian["Anak Perempuan"] = nilai * anak_p

    # ======================
    # CUCU (jika tidak ada anak)
    # ======================
    elif ada_cucu:
        unit = cucu_l * 2 + cucu_p
        if unit > 0:
            nilai = sisa / unit
            if cucu_l:
                bagian["Cucu Laki"] = nilai * 2 * cucu_l
            if cucu_p:
                bagian["Cucu Perempuan"] = nilai * cucu_p

    # ======================
    # SAUDARA (jika tidak ada anak & ayah)
    # ======================
    elif not ada_anak and not ayah:
        unit = saudara_l * 2 + saudara_p
        if unit > 0:
            nilai = sisa / unit
            if saudara_l:
                bagian["Saudara Laki"] = nilai * 2 * saudara_l
            if saudara_p:
                bagian["Saudara Perempuan"] = nilai * saudara_p

    # ======================
    # SISA KE AYAH / KAKEK
    # ======================
    else:
        if ayah:
            bagian["Ayah"] += sisa
        elif kakek:
            bagian["Kakek"] += sisa

    # ======================
    # OUTPUT
    # ======================
    print("\n=== HASIL ===")
    for k, v in bagian.items():
        print(f"{k}: Rp {v:,.2f}")


# Jalankan
hitung_waris()