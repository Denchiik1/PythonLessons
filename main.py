R = 5
n = 0
for x in range(-4, 5):
    for y in range(-4, 5):
        if x ** 2 + y ** 2 < R ** 2:
            n += 1
            print(x, y, n)