l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 22, 1024, 2228, 10728, 33859]
a = 2228
low = 0
high = len(l) - 1
def binary_search(a, l, low, high):
    if high == low or a > l[high]:
        return -1
    else:
        t = high // 2 + low // 2
        if a > l[t]:
            low = t
            return binary_search(a, l, low, high)
        elif a < l[t]:
            high = t
            return binary_search(a, l, low, high)
        elif a == l[t]:
            return t
print(binary_search(a, l, low, high))