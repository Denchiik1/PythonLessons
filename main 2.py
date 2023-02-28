f = open("C:\\Users\\danya\\Downloads\\17.txt")
s = f.read()
f.close()
s = s.split()
summ_par = 0
maks_znach = 0
l = [int(x) for x in s]
for i in range(len(l) - 1):
    x = l[i]
    y = l[i + 1]
    if x % 3 == 0 or y % 3 == 0:
        summ_par += 1
    if (x + y) > maks_znach:
        maks_znach = (x + y)
print(summ_par)
print(maks_znach)