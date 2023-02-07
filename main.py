def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n > 2:
        return F(n - 1) * n + F(n - 2) * (n - 1)
print(F(5))