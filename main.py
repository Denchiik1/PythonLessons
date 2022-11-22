s1 = '123456'
s = s1
l = 1
for i in range(0, len(s) - (l -1)):
    print(s[i: i + l])
for i in range(0, len(s) - l):
    print(s[i: i+ (l + 1)])
for i in range(0,  len(s) - (l + 1)):
    print(s[i: i + (l + 2)])
for i in range(0, len(s) - (l + 2)):
    print(s[i: i + (l + 3)])
for i in range(0, len(s) - (l + 3)):
    print(s[i: i + (l + 4)])