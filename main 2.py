position = 1
for n in range(5, 9):
    l = []
    for delit in range(2, n):
        if n % delit == 0:
            l.append(delit)
    if len(l) == 0:
        print(position, n)
    position += 1