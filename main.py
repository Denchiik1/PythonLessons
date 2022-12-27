f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\Питон\\Programm2.txt")
s = f.readlines()
f.close()
l = []
for x in s:
    a = x.split()
    if a[2] == "1":
        l.append(a[0])
        l.append(a[1])
summa = 0
for i in range(0, len(l), 2):
        t = int(l[i]) * int(l[i + 1])
        summa += t
print(summa)