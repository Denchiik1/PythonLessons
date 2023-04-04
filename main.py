def to_decimal(s, n):
    k = len(s) - 1
    s1 = 0
    i = 0
    while k >= 0:
        s1 += int(s[i]) * n ** k
        i += 1
        k -= 1
    return s1
def from_decime(x, n):
    s1 = 0
    l = []
    while x > n:
        x1 = x % n
        x = x // n
        l.append(x1)
    l.append(x)
    l.reverse()
    return l

def f(x, n1, n2):
    x2 = to_decimal(x, n1)
    return from_decime(x2, n2)
print(f('26', 8, 3))