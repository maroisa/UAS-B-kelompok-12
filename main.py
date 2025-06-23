import time
from rich.console import Console

from core.manajemen_produk import ManajemenProduk
from core import kalkulasi

def main():
    console = Console()
    manage = ManajemenProduk()
    manage.load_mock_data()
    while True:
        print ("")
        console.print("=" * 31,style="#FFD700")
        console.print(f"{'🍞 HANARI BAKERY 🍞':^30}", style="#FFD700")
        console.print("=" * 31,style="#FFD700")
        opsi_menu = {
    "1": {"teks": "Tambah Produk Baru", "warna": "#90EE90"},
    "2": {"teks": "Tampilkan Semua Produk", "warna": "#F4A460"},
    "3": {"teks": "Kalkulator Estimasi Profit", "warna": "#87CEFA"},
    "4": {"teks": "Simulasi Proses Produksi", "warna": "#4682B4"},
    "5": {"teks": "Keluar Dari Program", "warna": "#CD5C5C"}
}
        for opsi, menu in opsi_menu.items():
            console.print(f"{opsi}. {menu['teks']}")
        
        while True:
                try:
                    pilih_opsi = int(console.input("[#FFD700]Pilih opsi menu (1-5): [/#FFD700]"))
                    str_opsi = str(pilih_opsi)
                    if pilih_opsi not in range(1, 6):
                        console.print("[red]Pilihan tidak valid! Tolong masukan opsi 1 sampai 5![/red]")
                    else:
                        teks = opsi_menu[str_opsi]["teks"]
                        warna = opsi_menu[str_opsi]["warna"]
                        console.print(f"Anda memilih: [{warna}]{teks}[/{warna}]\n")
                        break
                except ValueError:
                    console.print("[red]Pilihan harus berupa angka![/red]")
        
        if pilih_opsi == 1:
             console.print("=" * 31,style="#FFD700")
             console.print(f"{'TAMBAH DATA PRODUK':^30}", style="#90EE90")
             console.print("=" * 31,style="#FFD700")
             manage.tambah_produk()
        elif pilih_opsi == 2:
             console.print("=" * 31,style="#FFD700")
             console.print(f"{'DAFTAR DATA PRODUK':^30}", style="#F4A460")
             console.print("=" * 31,style="#FFD700")
             manage.tampilkan_produk()

        elif pilih_opsi == 3:
             console.print("=" * 31,style="#FFD700")
             console.print(f"{'KALKULATOR ESTIMASI PROFIT':^30}", style="#87CEFA")
             console.print("=" * 31,style="#FFD700")
             for produk in manage.daftar_produk:
               console.print(f"[#87CEFA]{produk.kode}[/#87CEFA] - [white]{produk.nama}[/white]")
             if not manage.daftar_produk:
               console.print("[#CD5C5C]Belum ada produk yang ditambahkan.[/#CD5C5C]")
               continue
             kode = input("Masukkan kode produk: ").upper()
             produk = next((p for p in manage.daftar_produk if p.kode == kode), None)
             if produk:
               kalkulasi.input_produk(produk)
             else:
                 console.print("[#CD5C5C]Kode produk tidak ditemukan.[/#CD5C5C]")

        elif pilih_opsi == 4:
             console.print("=" * 31,style="#FFD700")
             console.print(f"{'SIMULASI PROSES PRODUKSI':^30}", style="#4682B4")
             console.print("=" * 31,style="#FFD700")
             for produk in manage.daftar_produk:
               console.print(f"[#87CEFA]{produk.kode}[/#87CEFA] - [white]{produk.nama}[/white]")
             if not manage.daftar_produk:
               console.print("[#CD5C5C]Belum ada produk yang ditambahkan.[/#CD5C5C]")
               continue
             kode = input("Masukkan kode produk: ").upper()
             produk = next((p for p in manage.daftar_produk if p.kode == kode), None)
             if produk:
                 kalkulasi.simulasi(produk)
             else:
                 console.print("[#CD5C5C]Kode produk tidak ditemukan.[/#CD5C5C]")

        elif pilih_opsi == 5:
             while True:
                  konfirmasi = console.input("\nYakin Ingin Keluar? ([#CD5C5C]yes[/#CD5C5C]/[#90EE90]no[/#90EE90]): ").replace(" ","").lower()
                  if konfirmasi == "yes":
                       print("Terima Kasih sudah menggunakan program Hanari Bakery")
                       print("Keluar dari program", end='', flush=True)
                       for _ in range(3):  
                         time.sleep(1)
                         print('.', end='', flush=True)
                       exit()
                  elif konfirmasi == "no":
                       print("Terima kasih sudah konfirmasi")
                       print("Kembali ke program", end='', flush=True)
                       for _ in range(3):  
                         time.sleep(1)
                         print('.', end='', flush=True)
                       break
                  elif konfirmasi not in ("yes", "no"):
                       console.print("[red]Pilihan tidak valid! Tolong masukan yes atau no![/red]")
                       continue
                  
if __name__ == "__main__":
    main()