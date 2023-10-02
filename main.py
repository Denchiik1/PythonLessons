import time
b = time.time()
k = 10000
a_prev = 1
S = a_prev
a_next = 0
for x in range(2, k + 1):
    a_next = a_prev / x
    S += a_next
    a_prev = a_next
l = time.time()
print(S)
print(l-b)