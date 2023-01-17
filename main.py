from math import sqrt
count = 0
b1 = 10
k1 = -1 / sqrt(3)
b2 = 0
k2 = 1 / sqrt(3)
tyash_chislo = (10 * sqrt(3)) / 2
for x in range(1, 809):
    for y in range(1, 10):
        if y > k2 * x + b2 and y < k1 * x + b1:
            count += 1
print(count)