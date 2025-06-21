from classes.roti.roti import Roti, abstractmethod
class KueKering(Roti):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        super().__init__(kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual)

    @abstractmethod
    def topping(self):
        pass