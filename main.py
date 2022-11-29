for a in range(174457, 174505):
    e = []
    for i in range(2, a):
        if a % i == 0:
            e.append(i)
    if len(e) == 2:
        print(e[0], e[1], sep='  ')