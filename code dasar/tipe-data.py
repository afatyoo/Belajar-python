
#data yang berbentuk angka
data_integer = 1
print(" data ", data_integer)
print(data_integer," adalah data: ", type(data_integer))
print("dikarenakan data ini adalah data yang berbentu angka")
print("")

#data yang berbentuk angka dengan koma 
data_float = 1.5
print ("data", data_float)
print(data_float, "adalah data:", type(data_float))
print("dikarenakan ini adalah data yang berbentuk desimal atau koma")
print("")


#angka yang berbentu karakter atau kumpulan karakter 
data_string = "data"
print("data", data_string)
print(data_string, "adalahh", type(data_string))
print("dikarenakan ini adalah data yang berbentu karakter atau huruf")
print("")


#data yang berbentuk bilangan binner 
data_bool = False
print ("data", data_bool)
print(data_bool, " adalah ", type(data_bool))
print("dikarenakan data ini adalah data 1 dan 0 yang memiliki output true atau false")
print("")

# bilangan kompleks
data_complex = complex(1+5)
print("data", data_complex)
print(data_complex, " adalah ", type(data_complex))
print("ini merupakan tipe data khusus")
print("")


#tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.10)
print("data", data_c_double)
print(data_c_double," adalah ", type(data_c_double))
print("")