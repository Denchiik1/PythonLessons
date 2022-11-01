word = input()
char = input()
count = 0
def f(word, char):
    if len(word) == 0:
        return False
    elif word[0] == char:
        return True
    else:
        return f(word[1:], char)
import time
b = time.time()
print(f(word, char))
print(time.time() - b)