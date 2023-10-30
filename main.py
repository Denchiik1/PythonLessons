l = "123"
def permut(l):
    ret = []
    if len(l) == 1:
        return l
    for i in range(len(l)):
        a = l[i]
        s = l[:i] + l[i+1:]
        r = permut(s)
        for x in r:
            ret.append(a + x)
    return ret
print(permut(l))