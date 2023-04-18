import math
def f(n):
    return []
def f(N):
    a = 0
    ret = [[N]]
    if N == 1:
        return ret
    for i in range(1, N):
        n = N - i
        l = f(n)
        for x in l:
            x.append(i)
        ret = ret + l
    return ret
m = f(16)
index = 0
maxp = 0
for i in range(len(m)):
    if math.prod(m[i]) >= maxp:
        index = i
        maxp= math.prod(m[i])
print(m[index])