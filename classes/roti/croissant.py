from classes.roti.roti import Roti
from interfaces.pengembangan import Pengembangan
import time
class Croissant(Roti, Pengembangan):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        super().__init__(kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual)

    def pengadonan(self):
        print("Mencampurkan tepung terigu protein tinggi, gula, ragi instan, garam, susu dingin, dan sedikit mentega.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Menguleni adonan hingga kalis elastis, kemudian dibentuk bulat dan bungkus plastik.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Mendiamkan adonan di kulkas")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)

    def pemanggangan(self):
        print("Memanaskan oven hingga suhu 190–200°C.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Mengoleskan permukaan croissant dengan telur")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Memanggang croissant hingga berwarna cokelat keemasan dan lapisannya terlihat mengembang dan renyah.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)

    def pengembangan(self):
        print("Menyiapkan mentega laminasi: pipihkan mentega dingin (bentuk persegi) untuk dilipat ke dalam adonan.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Menggilas adonan dan bungkus mentega di tengahnya.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Melakukan lipatan (turning): Melipat 3 atau 4 kali dan mengistirahatkan adonan di kulkas tiap kali di lipat.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Menggilas dan memotong adonan berbentuk segitiga, lalu menggulungnya membentuk croissant.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Memfermentasikan adonan yang sudah dibentuk di suhu ruang hingga mengembang dua kali lipat.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)

    def tampilkan_produk(self):
        print(f"Kode Produk: {self.kode}")
        print(f"Nama Produk: {self.nama}")
        print("Bahan Baku:")
        for b in self.daftar_bahan_baku:
            print(f"  - {b}")
        print(f"Biaya Produksi: Rp{self.biaya_produksi}")
        print(f"Harga Jual: Rp{self.harga_jual}")