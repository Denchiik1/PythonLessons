n = 0
r = 1
while r <= 114:
    n += 1
    r = bin(n)[2:]
    r += r[-1]
    if r.count("1") % 2 == 0:
        r += "0"
        if r.count("1") % 2 == 0:
            r += "0"
        else:
            r += "1"
    else:
        r += "1"
        if r.count("1") % 2 == 0:
            r += "0"
        else:
            r += "1"
    r = int(r, 2)
print(r)