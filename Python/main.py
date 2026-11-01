"""
UTS  Dasar Komputer dan Pemograman - Kelompok C (Instrumentasi)
Monitoring Level Tangki

Aturan status:
    Level < 30          -> LOW
    30 <= level <= 80   -> NORMAL
    level > 80          -> HIGH
"""

BATAS_BAWAH = 30
BATAS_ATAS = 80
DAFTAR_STATUS = ["LOW", "NORMAL", "HIGH"]

data_level = [
    18, 25, 33, 41, 55, 62, 76, 84, 91, 47, 29, 38, 70, 82, 15,   # data inti
    30, 80, 0, 100, 65.5                                          # data tambahan
]

def status_level(level):
    """Menentukan status level tangki (%) dan mengembalikannya sebagai string."""
    if level < BATAS_BAWAH:
        return "LOW"
    elif level <= BATAS_ATAS:
        return "NORMAL"
    else:
        return "HIGH"

def hitung_kategori(daftar_status):
    """Menghitung jumlah data pada tiap status; mengembalikan dictionary."""
    jumlah = {status: 0 for status in DAFTAR_STATUS}
    for status in daftar_status:
        jumlah[status]  += 1
    return jumlah

def rata_rata(data):
    """Menghitung rata-rata dari list angka."""
    return sum(data) / len(data)

def main():
    hasil_status = []
    print("==== MONITORING LEVEL TANGKI ====")
    for nomor, level in enumerate(data_level, start=1):
        status = status_level(level)
        hasil_status.append(status)
        print(f"{nomor:02d} level = {level:5.1f} % -> {status}")
    jumlah = hitung_kategori(hasil_status)

    print("\n===== RINGKASAN =====")
    print(f"Total data : {len(data_level)}")
    for status in DAFTAR_STATUS:
        print(f"Jumlah {status:<6}: {jumlah[status]}")
    print(f"Rata-rata : {rata_rata(data_level):.2f} %")
    print(f"Masksimum : {max(data_level):.1f} %")
    print(f"Minimum : {min(data_level):.1f} %")

if __name__ == "__main__":
    main()            