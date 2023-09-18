a = 250
s = ""
while a > 0:
    c = str(a % 16)
    if c == '10':
        c = 'A'
    elif c == '11':
        c = 'B'
    elif c == '12':
        c = 'C'
    elif c == '13':
        c = 'D'
    elif c == '14':
        c = 'E'
    elif c == '15':
        c = 'F'
    s = c + s
    a = a // 16
print(s)