# core/manajemen_produk.py
from rich.console import Console

from classes.roti.roti_manis import RotiManis
from classes.roti.croissant import Croissant
from classes.kue_kering.butter_cookies import ButterCookies
from classes.kue_kering.muffin import Muffin

from core.utils import input_pilihan, input_int

console=Console()
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

class ManajemenProduk:
    """Kelas untuk mengelola data produk roti/kue (tambah & tampil)."""
    def __init__(self):
        self.daftar_produk = []
    def load_mock_data(self):
        self.daftar_produk.extend([
            RotiManis(
                kode="RM001",
                nama="Roti Manis Susu",
                daftar_bahan_baku=[
                    "400 gr tepung cakra",
                    "100 gr tepung segitiga",
                    "10 gr ragi instant",
                    "100 gr gula pasir",
                    "3 kuning telur",
                    "250 ml susu cair dingin",
                    "110 gr mentega",
                    "½ sdt garam"
                ],
                biaya_produksi=50000 / 20,
                harga_jual=4000
            ),
            Croissant(
                kode="CR001",
                nama="Croissant Standar",
                daftar_bahan_baku=[
                    "525 gr tepung terigu serbaguna",
                    "250 ml air",
                    "125 ml susu cair",
                    "62 gr gula pasir",
                    "8 gr ragi instan",
                    "¼ sdt garam",
                    "315 gr mentega tawar",
                    "1 butir kuning telur"
                ],
                biaya_produksi=65000 / 12,
                harga_jual=6000
            ),
            ButterCookies(
                kode="BC001",
                nama="Butter Cookies(basic)",
                daftar_bahan_baku=[
                    "100 gr mentega tawar",
                    "55 gr gula halus",
                    "20 gr kuning telur",
                    "½ sdt vanilla extract",
                    "125 gr tepung serba guna",
                    "¼ sdt garam",
                    "100 gr Chocco chips"
                ],
                biaya_produksi=32500 / 15,
                harga_jual=3000
            ),
            Muffin(
                kode="MF001",
                nama="Muffin(basic)",
                daftar_bahan_baku=[
                    "250 gram tepung terigu",
                    "150 gram gula pasir",
                    "1/2 sdt garam",
                    "2 sdt baking powder",
                    "150 ml susu cair",
                    "2 butir telur ayam",
                    "150 gram margarin cair",
                    "1 sdt vanili"
                ],
                biaya_produksi=30000 / 15,
                harga_jual=3000
            )
        ])


    def tambah_produk(self):
        produk_map = {
            "1": ("Roti Manis", RotiManis),
            "2": ("Croissant", Croissant),
            "3": ("Butter Cookies", ButterCookies),
            "4": ("Muffin", Muffin)
        }
        for kode, (nama_produk, _) in produk_map.items():
            print(f"{kode}. {nama_produk}")
        pilihan = str(input_pilihan("Pilih jenis produk (1-4): ", 4))
        while True:
            kode=input("Masukkan Kode Produk: ").upper()
            if any(k.kode == kode for k in  self.daftar_produk):
                console.print(f'[Kode {kode}] sudah Terdaftar! Harap Masukkan kode dengan benar', style="#CD5C5C")
            else: break
        nama = input("Masukkan nama produk: ").title()
        jumlah = input_int("Masukkan jumlah produk sesuai bahan: ")
        while True:
            print(f"Masukkan bahan baku produk untuk {jumlah} pcs ")
            bahan = input_bahan_baku()
            if not bahan:
                console.print("Tidak ada bahan baku yang dimasukkan. Produk tidak dapat ditambahkan.", style="#CD5C5C")
                return
            else:
                break
        while True:
            biaya = input_int(f"Masukkan biaya produksi untuk {jumlah} pcs: ")
            if biaya < 0:
                console.print("Biaya produksi tidak boleh negatif.", style="#CD5C5C")
            else:
                break
        biaya_per_pcs = biaya / jumlah
        console.print(f"Biaya produksi per pcs: {biaya_per_pcs:.2f}", style="#90EE90")
        while True:
            harga = input_int("Masukkan harga jual untuk 1 pcs: ")
            if harga < biaya_per_pcs:
                console.print("Harga jual tidak boleh kurang dari biaya produksi.", style="#CD5C5C")
            else:
                break
        
        nama_produk, produk_class = produk_map[pilihan]
        produk = produk_class(kode, nama, bahan, biaya_per_pcs, harga)
        self.daftar_produk.append(produk)
        console.print(f"{nama_produk} '{produk.nama}' berhasil ditambahkan!\n", style="#90EE90")

    def tampilkan_produk(self):
        if not self.daftar_produk:
            print("Belum ada produk yang ditambahkan.")
            return

        for i, produk in enumerate(self.daftar_produk, 1):
            if isinstance(produk, RotiManis):
                print(f"\nJenis Produk {i}: Roti Manis")
            elif isinstance(produk, Croissant):
                print(f"\nJenis Produk {i}: Croissant")
            elif isinstance(produk, ButterCookies):
                print(f"\nJenis Produk {i}: Butter Cookies")
            elif isinstance(produk, Muffin):
                print(f"\nJenis Produk {i}: Muffin")
            else:
                console.print(f"\Jenis {i}: Produk Tidak Dikenal", style="#CD5C5C")
            print(f"\nProduk {i}: {produk.nama}")
            produk.tampilkan_produk()
