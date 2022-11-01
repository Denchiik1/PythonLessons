mas = dict()
def fib(n):
    if n < 3:
        return 1
    else:
        if n in mas:
            return mas[n]
        else:
            f = fib(n - 1) + fib(n - 2)
            mas[n] = f
            return f
import time
b = time.time()
print(fib(5))
print(time.time() - b)