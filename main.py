l = []
count = 0
abc = "ЕГЭ"
for x1 in abc:
    for x2 in abc:
        for x3 in abc:
            for x4 in abc:
                for x5 in abc:
                    if x1 in "ЕЭ":
                        s = x1 + x2 + x3 + x4 + x5
                        l.append(s)
                        count += 1
print(count)