f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\abapol.csv", encoding='utf8')
s = f.readlines()[1:]
f.close()
l = []
t1 = 0
arif = 0
kol_vo = 0
for x in s:
    l.append([int(y) for y in x.split(';')[2:]])
for x in l:
    if x[1] == 5 and (x[2] < 4 and x[2] != 0) and (x[3] < 4 and x[3] != 0):
        t1 += 1
    if x[0] == 5 and x[3] != 0:
        arif += x[3]
        kol_vo += 1
print(t1)
print(round(arif/kol_vo, 2))