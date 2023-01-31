x = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21
l = []
schetchik = 0
chw = []
while x > 0:
    a = x % 7
    x = x // 7
    l.append(a)
s = set(l)
print(len(s))