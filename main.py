f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\Питон\\Programm3.txt")
s = f.read()
f.close()
l = []
srednee_arif_count = 0
srednee_arif = 0
diometr = 1
diometr_count = 0
a = s.split()
for x in a:
    l.append(int(x))
for i in l:
    srednee_arif += i
    srednee_arif_count += 1
print(srednee_arif / srednee_arif_count)
for j in l:
    diometr *= j
    diometr_count += 1
print(diometr ** (1 / diometr_count))