f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\NewProgramm1.txt")
s = f.readlines()
f.close()
l = []
for k in s:
    l.append(int(k))
j = l[0]
for i in range(0, len(l)):
    if l[i] < j:
        j = l[i]
print(j)