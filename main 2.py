def f(x, y, z):
    x1 = int(str(x), y)
    s = ""
    while x1 > 0:
        c = str(x1 % z)
        s = c + s
        x1 = x1 // z
    return s
print(f(250, 8, 3))