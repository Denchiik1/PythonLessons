s = "346"
n = 7
def to_decime (s, n):
    k = len(s) - 1
    s1 = 0
    i = 0
    while k >= 0:
        s1 += int(s[i]) * n ** k
        i += 1
        k -= 1
    return s1
print(to_decime('346', 7))