s = input()
smas = s.split()
mas = [int(x) for x in smas]
l = [x for i, x in enumerate(mas) if i % 3 > 0]
print(l)