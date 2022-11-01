mas = [x for x in range(2, 10 ** 3) if x % 14 == 0]
import time
b = time.time()
print(mas)
print(time.time() - b)