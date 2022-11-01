x = input()
def f(s):
    m = set(list(s))
    sc = ""
    sb = ""
    sB = ""
    for x in m:
        if x.isdigit():
            sc += x
        elif not x.isdigit() and x.islower():
            sb += x
        elif not x.isdigit() and not x.islower() and x.isupper():
            sB += x
    sc = sc + sb + sB
    return sc
print(f(x))