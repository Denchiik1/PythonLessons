x = 2 * 216**6 + 3 * 36**9 - 432
l = []
schetchik = 0
chw = []
while x > 0:
    a = x % 6
    x = x // 6
    l.append(a)
s = set(l)
print(l.count(5))