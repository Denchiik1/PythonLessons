from math import sqrt

f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\Питон\\Programm3.txt")
s = f.read()
f.close()
l = []
srednee_arif_count = 0
srednee_arif = 0
D = 0
a = s.split()
for x in a:
    l.append(int(x))
for i in l:
    srednee_arif += i
    srednee_arif_count += 1
summa = srednee_arif
srednee_arif = srednee_arif / srednee_arif_count
for j in l:
    D += ((j - srednee_arif) ** 2) / len(l)
zabil_nazvanie_bukvi = sqrt(D)
print(zabil_nazvanie_bukvi)