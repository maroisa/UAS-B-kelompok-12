# core/manajemen_produk.py

from classes.roti.roti_manis import RotiManis
from classes.roti.croissant import Croissant
from classes.kue_kering.butter_cookies import ButterCookies
from classes.kue_kering.muffin import Muffin

def input_bahan_baku():
    bahan = []
    print("Masukkan bahan baku satu per satu (contoh: 'Tepung 200 gram')")
    print("Ketik 'selesai' jika sudah selesai.")
    
    while True:
        baris = input("  > ").strip()
        if baris.lower() == 'selesai':
            break
        if baris:
            bahan.append(baris)
    return bahan

class ManajemenProduk:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self):
        print("=== Tambah Produk Roti ===")
        print("1. Roti Manis")
        print("2. Croissant")
        print("3. Butter Cookies")
        print("4. Muffin")

        pilihan = input("Pilih jenis produk (1-4): ")

        kode = input("Masukkan kode produk: ")
        nama = input("Masukkan nama produk: ")
        bahan = input_bahan_baku()
        biaya = float(input("\nMasukkan biaya produksi: "))
        harga = float(input("Masukkan harga jual: "))

        if pilihan == "1":
            produk = RotiManis(kode, nama, bahan, biaya, harga)
        elif pilihan == "2":
            produk = Croissant(kode, nama, bahan, biaya, harga)
        elif pilihan == "3":
            produk = ButterCookies(kode, nama, bahan, biaya, harga)
        elif pilihan == "4":
            produk = Muffin(kode,nama,bahan,biaya,harga)
        else:
            print("Pilihan tidak valid.")
            return

        self.daftar_produk.append(produk)
        print(f"Produk '{produk.nama}' berhasil ditambahkan!\n")

    def tampilkan_produk(self):
        if not self.daftar_produk:
            print("Belum ada produk yang ditambahkan.")
            return

        print("\n=== Daftar Produk ===")
        for i, produk in enumerate(self.daftar_produk, 1):
            print(f"\nProduk {i}:")
            produk.tampilkan_produk()
