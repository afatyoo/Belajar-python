def kelvin_program():
    print("\n PROGRAM KONVERSI TEMEPRATUR KELVIN\n")

    kelvin = float(input("Masukan suhu dalam kelvin:"))
    print("Suhu adalah", kelvin, "kelvin")

#celcius 
    celcius = kelvin - 273
    print("suhu dalam celcius adalah", celcius, "celcius")

# reamur
    reamur = ((4/5) * kelvin) - 273
    print("suhu dalam reamur adalah", reamur, "reamur")

# farenheit 
    farenheit1 = celcius
    farenheit_asli = ((9/5) * farenheit1) + 32

    print("suhu dalam farenheit adalah", farenheit_asli, "Farentheit")