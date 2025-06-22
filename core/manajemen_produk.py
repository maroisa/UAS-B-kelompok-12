# core/manajemen_produk.py

from classes.roti.roti_manis import RotiManis
from classes.roti.croissant import Croissant
from classes.kue_kering.butter_cookies import ButterCookies
from classes.kue_kering.muffin import Muffin

def input_bahan_baku():
    bahan = []
    print("\nMasukkan bahan baku satu per satu (contoh: 'Tepung 200 gram')")
    print("Ketik 'selesai' atau tekan [ENTER] jika sudah selesai.")
    
    while True:
        baris = input("  > ").strip()
        if baris.lower() == 'selesai' or baris == '':
            break
        if baris:
            bahan.append(baris)
    return bahan

def input_int(prompt):
    while True:
        try:
            nilai = int(input(prompt))
            if nilai < 0:
                print("Input tidak boleh negatif.")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid. Harap masukkan angka!")

class ManajemenProduk:
    """Kelas untuk mengelola data produk roti/kue (tambah & tampil)."""
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self):
        produk_map = {
            "1": ("Roti Manis", RotiManis),
            "2": ("Croissant", Croissant),
            "3": ("Butter Cookies", ButterCookies),
            "4": ("Muffin", Muffin)
        }
        for kode, (nama_produk, _) in produk_map.items():
            print(f"{kode}. {nama_produk}")
        while True:
            pilihan = input("Pilih jenis produk (1-4): ")
            if pilihan not in produk_map:
                print("Produk tidak valid. Harap masukkan angka 1-4.")
            else:
                break
        while True:
            kode=input("Masukkan Kode Produk: ").upper()
            if any(k.kode == kode for k in  self.daftar_produk):
                print(f'[Kode {kode}] sudah Terdaftar! Harap Masukkan kode dengan benar')
            else: break
        nama = input("Masukkan nama produk: ").title()
        while True:
            bahan = input_bahan_baku()
            if not bahan:
                print("Tidak ada bahan baku yang dimasukkan. Produk tidak dapat ditambahkan.")
                return
            else:
                break
        biaya = input_int("Masukkan biaya produksi: ")
        while True:
            harga = input_int("Masukkan harga jual: ")
            if harga < biaya:
                print("Harga jual tidak boleh kurang dari biaya produksi.")
            else:
                break
        
        nama_produk, produk_class = produk_map[pilihan]
        produk = produk_class(kode, nama, bahan, biaya, harga)
        self.daftar_produk.append(produk)
        print(f"{nama_produk} '{produk.nama}' berhasil ditambahkan!\n")

    def tampilkan_produk(self):
        if not self.daftar_produk:
            print("Belum ada produk yang ditambahkan.")
            return

        print("\n=== Daftar Produk ===")
        for i, produk in enumerate(self.daftar_produk, 1):
            print(f"\nProduk {i}:")
            produk.tampilkan_produk()
