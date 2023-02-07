def F(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return F(n // 2)
    else:
        return 1 + F(n - 1)
l = []
for x in range(1, 1001):
    if F(x) == 3:
        l.append(x)
print(len(l))