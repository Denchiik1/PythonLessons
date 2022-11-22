s1 = open("C:\\Users\\danya\\OneDrive\\Документы\\24.txt")
s = s1.read()
s1.close()
l = []
i = 0
k = 1
for j in range(1, len(s)):
    if s[j] != s[j - 1]:
        k += 1
    else:
        l.append(j - i)
        i = j
print(max(l))