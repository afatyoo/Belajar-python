from tambah import tambah
from bagi import bagi
from kurang import kurang
from kali import kali

def main():
    print("")
print(20*"=")
print("KALKULATOR SEDERHANA BY TYOCHANNN")
print("ini adalah kalkulator sederhana yang hanya memasukan dua angka")
print(20*"=")

print("\npilih jenis operator:")
print("1. Tambah", flush=(True))
print("2. Kurang", flush=(True))
print("3. Kali", flush=(True))
print("4. Bagi", flush=(True))
pilih_operator = input(" masukan operator yang anda mau:")

if pilih_operator == '1' :
    tambah()
elif pilih_operator == '2' :
    kurang()
elif pilih_operator == '3' :
    kali()
elif pilih_operator == '4' :
    bagi()
else :
    print("salah operator program berakhir")

print(100*"=")




