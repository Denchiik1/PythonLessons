s = input()
smas = s.split()
mas = [int(x) for x in smas]
l = [str(x) + str(x) for x in mas if len(str(x)) == 2]
mas = [int(x) for x in l]
print(mas)