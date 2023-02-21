f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\Питон\\21.02.23_5.txt")
s = f.read()
f.close()
count = 0
l = []
for x in range(0, len(s) - 2):
    if s[x] == s[x + 2]:
        l.append(s[x + 1])
l1 = set(l)
for x in l1:
    print(x, l.count(x))