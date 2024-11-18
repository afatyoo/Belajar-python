sisi = 8

# emnggunakan for 
# variable dummy 
print(" awal menggunakan for")
count = 1 
for i in range(sisi):
    print("*"*count)
    count += 1

print(" akhir menggunakan for")
print("")
print(" awal menggunakan while")
# Menggunakan while 
count = 1
while True:
    print ("*"*count)
    count += 1

    if count > sisi:
        break

print(" akhir menggunakan while")
print("")


# hanya untuk angka ganjil saja 

print("")
print(" awal menggunakan while")
# Menggunakan while 
count = 1
while True:
    if (count%2):
        print ("*"*count)
        count += 1
    else: 
        count += 1
        continue
    if count > sisi:
        break

print(" akhir menggunakan while")
print("")


# print segitiga 
print("")
print(" awal menggunakan while")
# Menggunakan while 
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print (" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else: 
        count += 1
        continue
    if count > sisi:
        break

print(" akhir menggunakan while")
print("")

# print ketupat
print("")
print(" awal menggunakan while")
# Menggunakan while 
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print (" "*spasi,"*"*count)
        spasi -= 1
        count += 1
    else: 
        count += 1
        continue
    if count > sisi:
        break

while True:
    if (count%2):
        spasi += 1
        print (" "*spasi,"*"*count)
        count -= 1
    else:
        count -=1 
        continue
    if count == 0 :
        break

print(" akhir menggunakan while")
print("")






















































































