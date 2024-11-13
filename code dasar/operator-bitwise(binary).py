# menentukan bilangan binary

a = 100
b = 200
print("\n=====OR=====")
#  bitwize or (|)
c = a | b
print("Berikut adalah angka binarry ", a,"=", format(a,'08b'))
print("Berikut adalah angka binarry ", b,"=", format(b,'08b'))

print("Berikut adalah angka bitwise or dari keduanya ", c,"=", format(c,'08b'))

print("\n=====AND=====")
#  bitwize and (&)
c = a & b
print("Berikut adalah angka binarry ", a,"=", format(a,'08b'))
print("Berikut adalah angka binarry ", b,"=", format(b,'08b'))

print("Berikut adalah angka bitwise AND dari keduanya ", c,"=", format(c,'08b'))

print("\n=====XOR=====")
#  bitwize XOR (^)
c = a ^ b
print("Berikut adalah angka binarry ", a,"=", format(a,'08b'))
print("Berikut adalah angka binarry ", b,"=", format(b,'08b'))

print("Berikut adalah angka bitwise XOR dari keduanya ", c,"=", format(c,'08b'))

print("\n=====NOT=====")
#  bitwize NOT (~) PERLU DI UBAH TERLEBIH DAHULU MENGGUNAKAN OPERATOR XOR
c = ~a
e = 0b00001010
d = 0b11111111
print("Berikut adalah angka binarry ", a,"=", format(a,'08b'))

print("Berikut adalah angka bitwise NOT dari keduanya ", e^d,"=", format(e^d,'08b'))

print("\n=====SHIFTING=====")

print("\n Shitfing right")
#  bitwize SHIFTING ke kanan (>>)
c = a >> 1
print("Berikut adalah angka binarry ", c,"=", format(c,'08b'))

print("\n Shitfing left")
#  bitwize SHIFTING ke kanan (<<)
c = a << 1
print("Berikut adalah angka binarry ", c,"=", format(c,'08b'))
