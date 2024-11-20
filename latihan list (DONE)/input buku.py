# ini adalah program untuk list karyawan

print("="*20,"Masukan krayawan baru","="*20)

list_karyawan = []

while True: 
    print("\nMasukan karyawan baru")
    nama_karyawan = input("Masukan nama karyawan: ")
    umur_karuawan = input("Masukan umur karyawan: ")

    karyawan_baru = [nama_karyawan,umur_karuawan]
    list_karyawan.append(karyawan_baru)

    print("\nBerikut adalah karyawan baru")
    for index,karyawan_baru in enumerate(list_karyawan):
            print(f"{index+1} | Nama = {karyawan_baru[0]} | Umur = {karyawan_baru[1]}tahun  ")

    print("="*30)
    Lanjut = input("Apakah ada karyawan baru ? (y/n)")

    if Lanjut == "n" :
        break
print("="*20,"PROGRAM SELESAI", "="*20)