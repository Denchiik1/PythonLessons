f = open("C:\\Users\\danya\\Downloads\\17 (1).txt")
s = f.read()
f.close()
s = s.split()
summ_par = 0
maks_znach = 0
l = [int(x) for x in s]
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        x = l[i]
        y = l[j]
        if (x % 160 != y % 160) and (x % 7 == 0 or y % 7 == 0):
            summ_par += 1
            if x + y > maks_znach:
                maks_znach = x + y
print(summ_par)
print(maks_znach)