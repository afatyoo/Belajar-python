import os 


def fungsi_header():
    os.system("cls")
    print(f"{"PROGRAM FUNGSI":^50}")
    print(f"{"BY TYOCHANNN":^50}")
    print(f"{"-"*50:^50}")

def input_user():
    lebar = int(input(" Masukan Lebar = "))
    panjang = int(input(" Masukan Panjang = "))
    
    return lebar,panjang


def hitung_luas(lebar,panjang):
    return lebar * panjang


def hitung_keliling(lebar,panjang):
    return 2 * (lebar + panjang)



fungsi_header()

while True:
    fungsi_header()
    print("1.LUAS")
    print("2.KELILING")
    opsi = (input("Masukan Opsi Kamu: "))
    
    if opsi == "1":
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        #print(LUAS)
        print(f"hasil luas = {LUAS}")
    elif opsi == "2":
        LEBAR,PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR,PANJANG)
        #print(KELILING)
        print(f"hasil keliling = {KELILING}")



    isContinue = input("apakah kamu mau lanjut (y/n)")
    if isContinue == "n":
        break