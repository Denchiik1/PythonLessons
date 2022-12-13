f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\25.txt")
s = f.readlines()
f.close()
d = s[0].split()
d = int(d[0])
l = []
i = 0
summa = 0
last = 0
for k in range(1, len(s)):
    l.append(int(s[k]))
l.sort()
summ = 0
while summ < d:
    i += 1
    summ = sum(l[:i])
print(d, i)
summ = sum(l[:i - 1])
k = i - 2
t = i - 1
summ = summ - l[k] + l[t]
while summ < d:
    k += 1
    t += 1
    summ = summ - l[k] + l[t]
print(l[k])