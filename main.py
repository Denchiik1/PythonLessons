s1 = open("C:\\Users\\danya\\OneDrive\\Изображения\\Telegram\\inf24.txt")
s = s1.readlines()
s1.close()
l = []
k = 0
for j in s:
    l.append(j.count("G"))
m = l[0]
for i in range(len(l)):
    if l[i] > m:
        m = l[i]
        k = i
print(s[k])