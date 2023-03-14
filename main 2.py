for n in range(174457, 174505):
    l = []
    for delit in range(2, n):
        if n % delit == 0:
            l.append(delit)
    if len(l) == 2:
            print(l[0], l[1])