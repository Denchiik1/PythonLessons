f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\Питон\\Programm4.txt")
s = f.readlines()
f.close()
l = []
a = 0
for x in s:
    a = x.split()
    l.append(a)
for i in l:
    if int(i[0]) * int(i[1]) >= 0:
        print(i[0], i[1])