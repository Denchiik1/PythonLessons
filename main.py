s = input()
smas = s.split()
mas = [int(x) for x in smas]
l = [x for x in mas if len(str(x)) % 2 != 0]
print(l)