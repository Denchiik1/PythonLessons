mas = []
for x in range(2, 10 ** 6):
    if x % 2 > 0:
        mas.append(x)
import time
b = time.time()
print(mas)
print(time.time() - b)
