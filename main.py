l = []
count = 0
abc = "ABCX"
for x1 in abc:
    if x1 == "X":
        for x2 in abc:
            for x3 in abc:
                for x4 in abc:
                    for x5 in abc:
                        if x2 != "X" and x3 != "X" and x4 != "X" and x5 != "X":
                                s = x1 + x2 + x3 + x4 + x5
                                l.append(s)
                                count += 1
    else:
        for x2 in abc:
            for x3 in abc:
                for x4 in abc:
                    for x5 in abc:
                        if x2 != "X" and x3 != "X" and x4 != "X" and x5 != "X":
                            s = x1 + x2 + x3 + x4 + x5
                            l.append(s)
                            count += 1
print(count)