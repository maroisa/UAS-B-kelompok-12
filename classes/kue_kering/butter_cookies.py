from classes.kue_kering.kue_kering import KueKering
import time
class ButterCookies(KueKering):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        super().__init__(kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual)

    def pengadonan(self):
        print("Menyiapkan bahan")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
        print("Mencampur bahan.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
        print("Mendiamkan adonan di kulkas.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
       
    def pemanggangan(self):
        print("Memanaskan oven pada suhu 160–180°C.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
        print("Menyiapkan loyang yang diberi alas dengan kertas baking/parchment.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
        print("membentuk adonan dan menatanya di atas loyang.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
        print("Memanggang cookies hingga pinggiran cookies berwarna keemasan.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
        print("Mengeluarkan cookies dari oven")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()

    def topping(self):
        print("mendinginkan cookies di rak kawat.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
        print("Menyiapkan topping")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print()
        print("Memberikan hiasan dengan topping")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
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