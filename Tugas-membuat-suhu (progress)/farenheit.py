print("\nPROGRAM KONVERSI TEMPERATUR UNTUK Farenheit")

farenheit = float(input("Masukan suhu dalam farenheit: "))
print("suhu adalah", farenheit, "Farenheit")

# reamur
reamur = (4/9) * (farenheit - 32)
print("Suhu adalah", reamur, "reamur")

# cecius 
celcius = (5/9) *  (farenheit - 32)
print("suhu dalam celcius ", celcius, "Celcius")

# kelvin
kelvin_konvert = celcius 
kelvin_asli = kelvin_konvert + 273
print ("Suhu dalam kelvin", kelvin_asli, "Kelvin")