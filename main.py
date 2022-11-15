s = input()
mas = "0123456789"
mas2 = "qwertyuiopasdfghjklzxcvbnm"
d = ""
i = 0
while i < len(s):
    if s[i] == 'a' and s[i+1] == 'a':
        d += '*'
        i += 2
    else:
        d += s[i]
        i += 1
print(d)