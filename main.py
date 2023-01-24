count = 0
count1 = 0
count2 = 0
b1 = 12
k1 = -1/3**0.5
b2 = 0
k2 = 1/3**0.5

for x in range(1, 12):
    for y in range(1, 12):
        if not (k1 * x + b1 > y and k2 * x + b2 < y):
            count += 1

print(count)