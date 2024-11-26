# Date and time (latihan)

import datetime as waktu

print("Silahkan masukan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal lahir anda\t: "))
bulan = int(input("Bulan lahir anda \t\t: "))
tahun = int(input("Tahun lahir anda\t\t: "))

tanggal_lahir = waktu.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

hari_ini = waktu.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")

