# comtinue dan pass

# pass berfungsi sebagai dummy yang tidak akan di eksekusi 


# ini adalah fungsi pass yang dimana akan menjadi dummy dan tidak akan dieksekusi

angka = 1

while angka < 10: 
    angka += 2
    
    if angka == 3:
        print(f"angka sudah mencapai {angka}")
        pass
    print(angka)


# ini adalah sample continue 

angka = 0

print(f"angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")

    if angka == 3:
        print("nice!") 
        continue # fungsi continue akan langsung loncat ke awal code jika setelah continue
    print("whassup!")

print("Pinish!")

    

