# merubah data atau casting data pada python
print("====INTEGER====")
data_int = 10 

print("data", data_int, "adalah", type(data_int))
print("")
data_float = float(data_int)
data_bool = bool(data_int)
data_str = str(data_int)
print("ini adalah hasil casting data ke float", data_float, type(data_float))
print("")
print("ini adalah hasil casting data ke bolean", data_bool, type(data_bool))
print("")
print("ini adalah hasil casting data ke string", data_str, type(data_str))


print("====FLOAT====")
data_float = 1.0

print("data", data_float, "adalah", type(data_float))
print("")
data_int = int(data_float)
data_bool = bool(data_float)
data_str = str(data_float)
print("ini adalah hasil casting data ke integer", data_int, type(data_int))
print("")
print("ini adalah hasil casting data ke bolean", data_bool, type(data_bool))
print("")
print("ini adalah hasil casting data ke string", data_str, type(data_str))



print("====BOLEAN====")
data_bool = True

print("data", data_bool, "adalah", type(data_bool))
print("")
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("ini adalah hasil casting data ke integer", data_int, type(data_int))
print("")
print("ini adalah hasil casting data ke float", data_float, type(data_float))
print("")
print("ini adalah hasil casting data ke string", data_str, type(data_str))


print("====STRING====")
data_str = "Kamu suka aku"

print("data", data_str, "adalah", type(data_str))
print("")
data_int = int(data_str) #data string tidak bisa di ubah menjadi integer
data_bool = bool(data_str)  #jika memiliki data seperti isi nya itu akan di definiskan true dan jika data nya kosong maka false
data_float = float(data_str)# tidak bisa diuabah dari string
print("ini adalah hasil casting data ke integer", data_int, type(data_int))
print("")
print("ini adalah hasil casting data ke float", data_bool, type(data_bool))
print("")
print("ini adalah hasil casting data ke string", data_float, type(data_float))
