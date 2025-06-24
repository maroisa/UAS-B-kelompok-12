from rich.prompt import Prompt
from rich.console import Console

console = Console()
def input_pilihan(message: str, pilihanNum: int):
    while True:
        pilihan = input_int(message)
        if pilihan in range(1, pilihanNum + 1): return pilihan
        else:
            console.print(f"Pilihan tidak valid. Harap masukkan salah satu dari {tuple(range(1, pilihanNum + 1))}.",style="#CD5C5C")


def input_int(message: str):
    while True:
        nilai = Prompt.ask(f"{message}")
        try: 
            nilai = int(nilai)
            return nilai
        except: 
            console.print("Input harus berupa angka!",style="#CD5C5C")
            continue


def format_rupiah(angka):
    return f"Rp{int(angka):,}".replace(",", ".")