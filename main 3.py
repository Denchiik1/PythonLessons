f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\Питон\\21.02.2023_3.txt")
s = f.read()
f.close()
m = 0
k = 1
for x in range(0, len(s) - 1):
    if s[x] == "A" and s[x + 1] == "A":
        k += 1
    else:
        m = max(k, m)
        k = 1
print(m)