a = 36
s = ""
while a > 0:
    c = str(a % 2)
    s = c + s
    a = a // 2
print(s)