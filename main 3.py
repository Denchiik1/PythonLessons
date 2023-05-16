n = 0
r = 1
maximum = 0
while n <= 1000:
    n += 1
    r = bin(n)[2:]
    r = r[::-1]
    r = int(r, 2)
    if r == 23 and n > maximum:
        maximum = n
print(maximum)