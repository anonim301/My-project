#======
#ANALIS NILAI
#=======

def konversi_nilai(nilai):
  if nilai >= 90:
    return "A"
  elif nilai >= 80:
    return "B"
  elif nilai >= 70:
    return "C"
  elif nilai >= 60:
    return "D"
  else:
    return "E"

def analis_nilai(daftar_nilai):
    jumlah_siswa = len(daftar_nilai)
    max_nilai = max(daftar_nilai)
    min_nilai = min(daftar_nilai)
    average_nilai = sum(daftar_nilai) / jumlah_siswa
    lulus = [n for n in daftar_nilai if n >= 75]
    tidak_lulus = [n for n in daftar_nilai if n < 75]
    jumlah_lulus = len(lulus)
    jumlah_tidak_lulus = len(tidak_lulus)
    presentase_kelulusan = (jumlah_lulus / jumlah_siswa) * 100
    up_average_nilai = [n for n in daftar_nilai if n  > average_nilai ]

    #output utama
    print("ANALISIS NILAI SISWA")
    print("=" * 25)
    print(f"Jumlah siswa        : {jumlah_siswa}")
    print(f"Nilai tertinggi     : {max_nilai}")
    print(f"Nilai terendah      : {min_nilai}")
    print(f"Rata-rata           : {average_nilai:.2f}")
    print(f"Jumlah lulus (>=75) : {jumlah_lulus}")
    print(f"Tidak lulus (<75)   : {jumlah_tidak_lulus}")
    print(f"Persentase lulus    : {presentase_kelulusan:.2f}%")
    print(f"Nilai di atas rata  : {up_average_nilai}")

    #konversi ke huruf
    print("\nKonversi Nilai ke Huruf")
    for i,nilai in enumerate(daftar_nilai,start=1):
      huruf = konversi_nilai(nilai)
      print(f"Siswa {i}: {nilai} -> {huruf}")

    # Histogram sederhana
    print("\nHistogram Nilai (ASCII):")
    kategori = {
        "0-59  (E)": 0,
        "60-69 (D)": 0,
        "70-79 (C)": 0,
        "80-89 (B)": 0,
        "90-100(A)": 0
    }

    for nilai in daftar_nilai:
        if nilai < 60:
            kategori["0-59  (E)"] += 1
        elif nilai < 70:
            kategori["60-69 (D)"] += 1
        elif nilai < 80:
            kategori["70-79 (C)"] += 1
        elif nilai < 90:
            kategori["80-89 (B)"] += 1
        else:
            kategori["90-100(A)"] += 1

    for k, v in kategori.items():
        print(f"{k} : {'*' * v} ({v})")


# ===== INPUT DATA =====
# Contoh data nilai (bisa kamu ganti)
nilai_siswa = [85, 90, 70, 60, 75, 88, 92, 55, 78, 83]

# Jalankan analisis
analis_nilai(nilai_siswa)
