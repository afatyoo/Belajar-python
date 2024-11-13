data = input("silahkan masukan data: ")

print("Hasil input ", data, "dan tipe", type(data))

data_int = int(input("silahkan masukan angka: "))
data_float = float(input("silahkan masukan angka lagi : "))

print("Hasil input ", data_int, "dan tipe", type(data_int))

print("Hasil input ", data_float, "dan tipe", type(data_float))

# untuk imputan dari bolean dikarenakan dia hanya dua nilai jadi perlu di casting ke integer terlebih dahulu contoh

binner = bool(int(input("Masukan angka: ")))

print("Hasil input: ", binner, "dan tipe", type(binner) )



