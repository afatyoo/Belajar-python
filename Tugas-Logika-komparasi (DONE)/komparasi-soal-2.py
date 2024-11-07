inputangka = float(input("Masukan angka\n 1.kurang dari 0 dan lebih dari 5\n dan \n 2.kurang dari 8 dan lebih dari 11\n Masukan angka:"))

rule1 = inputangka < 0
rule2 = inputangka > 5
rule3 = inputangka < 8 
rule4 = inputangka > 11

hasil1 = rule1 or rule2

hasil2 =  rule3 or rule4
 
hasil3 = hasil1 and hasil2    

print("hasil 1", hasil1)
print("hasil 2", hasil2)
print("hasil semuanya:", hasil3)