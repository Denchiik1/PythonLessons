for n in range(110203, 110246):
    l = []
    for delit in range(2, n + 1, 2):
        if n % delit == 0:
            l.append(delit)
    if len(l) == 4:
        print(l[0], l[1], l[2], l[3])