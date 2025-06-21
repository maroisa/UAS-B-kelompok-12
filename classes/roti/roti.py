from abc import ABC, abstractmethod
class Roti(ABC):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        self.kode = kode
        self.nama = nama
        self.daftar_bahan_baku = daftar_bahan_baku
        self.biaya_produksi = biaya_produksi
        self.harga_jual = harga_jual

    @abstractmethod
    def pengadonan(self):
        pass

    @abstractmethod
    def pemanggangan(self):
        pass

    @abstractmethod
    def tampilkan_produk(self):
        pass