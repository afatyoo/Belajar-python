inputangka = float(input("Masukan angka\n  lebih dari 0 dan kurang dari 5\n dan \n lebih dari 8 kurang dari 11\n Masukan angka:"))

rule1 = inputangka > 0
rule2 = inputangka < 5
rule3 = inputangka > 8 
rule4 = inputangka < 11

hasil1 = rule1 and rule2
hasil2 = rule3 and rule4

print("lebih dari 0 dan kurang dari 5", hasil1)

print("lebih dari 8 dan kurang dari 11", hasil2)

print("hasil semuanya:", hasil1 or hasil2)
