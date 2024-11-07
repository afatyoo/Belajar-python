from celcius import celcius_program
from kelvin import kelvin_program
from reamur import reamur_program
from farenheit import farenheit_program

def main():
    print("")
print("\npilih jenis konversi suhu:")
print("1. celcius", flush=(True))
print("2. farenheit", flush=(True))
print("3. kelvin", flush=(True))
print("4. reamur", flush=(True))

choice = input("masukan pilhan (1-4) :")

if choice == '1':
    celcius_program()
elif choice == '2':
    farenheit_program()
elif choice == '3':
    kelvin_program()
elif choice == '4':
    reamur_program()
else:
    print("Pilihan kamu tidak valid")

if __name__ == "__name__":
    main()
