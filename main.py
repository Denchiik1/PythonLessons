f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\Питон\\24_demo.txt")
s = f.read()
f.close()
count = 0
m = 0
k = 1
for x in range(1, len(s) - 1):
    if s[x] != s[x + 1]:
        k += 1
    else:
        m = max(k, m)
        k = 1
print(m)