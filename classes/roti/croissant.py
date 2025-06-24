from classes.roti.roti import Roti
from interfaces.pengembangan import Pengembangan
import time
class Croissant(Roti, Pengembangan):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        super().__init__(kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual)

    def pengadonan(self):
        print("Menyiapkan bahan")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Mencampurkan bahan.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Menguleni adonan hingga kalis elastis, kemudian dibentuk bulat dan bungkus plastik.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Mendiamkan adonan di kulkas")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()

    def pemanggangan(self):
        print("Memanaskan oven hingga suhu 190–200°C.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Memanggang croissant hingga berwarna cokelat keemasan dan lapisannya terlihat mengembang dan renyah.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Mengangkat dan mendinginkan croissant.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()

    def pengembangan(self):
        print("Menggilas adonan di tengahnya.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Melakukan lipatan (turning): Melipat 3 atau 4 kali dan mengistirahatkan adonan di kulkas tiap kali di lipat.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Menggilas dan memotong adonan berbentuk segitiga, lalu menggulungnya membentuk croissant.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Memfermentasikan adonan yang sudah dibentuk di suhu ruang hingga mengembang dua kali lipat.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()

    def tampilkan_produk(self):
        print(f"Kode Produk: {self.kode}")
        print(f"Nama Produk: {self.nama}")
        print("Bahan Baku:")
        for b in self.daftar_bahan_baku:
            print(f"  - {b}")
        print(f"Biaya Produksi: Rp{self.biaya_produksi} per pcs")
        print(f"Harga Jual: Rp{self.harga_jual} per pcs")