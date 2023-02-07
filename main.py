s = '9' * 85
while ('666' in s) or ('999' in s):
    if '666' in s:
        s = s.replace('666', '9', 1)
    else:
        s = s.replace('999', '6', 1)
print(s)