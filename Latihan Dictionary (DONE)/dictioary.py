import datetime
import os
import string
import random

data_template = {
    'nama':'nama',
    'nis':00000000,
    'lahir':datetime.datetime(1111,1,11),
    'beasiswa':'beasiswa'
}

data_siswa_baru = {}

os.system("cls")
while True: 
    print(f"{'SELAMAT DATANG SISWA BARU':^30}")
    print(f"{'DATA SISWA BARU':^30}") 
    print("-"*40)

    data_siswa = dict.fromkeys(data_template.keys())
    data_siswa['nama'] = input("Masukan nama siswa: ")
    data_siswa['nis'] = int(input("Masukan NIS: "))
    TAHUN = int(input('Masukan Tahun Lahir Anda (YYYY): '))
    BULAN = int(input('Masukan Bulan Lahir Anda (1-12): '))
    TANGGAL = int(input('Masukan Tanggal Lahir Anda (1-30): '))
    data_siswa ['lahir'] = datetime.datetime(TAHUN,BULAN,TANGGAL)
    data_siswa['beasiswa'] = input("Apakah kamu punya beasiswa: ")


    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_siswa_baru.update({KEY:data_siswa})
    print(f"{'KEY':<6} {'NAMA':<17} {'NIS':<9}  {'BEASISWA':^7} {'LAHIR':<10}")
    print('-'*100)
    for data_siswa in data_siswa_baru:
        KEY = data_siswa

        NAMA = data_siswa_baru[KEY]['nama']
        NIS = data_siswa_baru[KEY]['nis']
        BEASISWA = data_siswa_baru[KEY]['beasiswa']
        LAHIR = data_siswa_baru[KEY]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {NIS:<9}  {BEASISWA:^7} {LAHIR:<10}")

    print('\n')
    done = input("apakah sudah tidak ada siswa baru? (Y/N) ")
    if done == "Y":
        break

print(f"\n Terimakasih")

