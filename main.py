n = 0
k1 = 1.5
b1 = 0
b2 = 4.5
k2 = -0.75
count = 0
for x in range(1, 3):
    for y in range(1, 3):
        if k1 * x + b1 > y:
            print(x, y)
            count += 1
for x in range(3, 6):
    for y in range(1, 3):
        if k2 * x + b2 > y:
            print(x, y)
            count += 1
print(count)