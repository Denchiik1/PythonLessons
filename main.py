l = []
prov = 1
while prov > 0:
    chislo = int(input())
    if chislo > 9 and chislo < 100:
        l.append(chislo)
    prov = chislo
obsh = 0
for y in l:
    obsh += y
if obsh == 0:
    print("NO")
else:
    print(obsh / len(l))