n = 0
r = 1
while r <= 68:
    n += 1
    r = bin(n)[2:]
    if r.count("1") % 2 == 0:
        r += "0"
        r = "101" + r[3:]
    else:
        r += "11"
        r = "10" + r[2:]
    r = int(r, 2)
print(n)