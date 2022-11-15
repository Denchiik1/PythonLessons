s = input()
def f(s):
    m = set()
    for x in s:
        m.add(x)
    for i in s:
        if s.count(i) > len(m):
            return False
        else:
            return True
print(f(s))