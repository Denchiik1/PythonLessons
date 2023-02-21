f = open("C:\\Users\\danya\\OneDrive\\Рабочий стол\\Питон\\inf_22_10_20_24.txt")
s = f.readlines()
f.close()
k = 0
for x in s:
    if x.count("E") > x.count("A"):
        k += 1
print(k)