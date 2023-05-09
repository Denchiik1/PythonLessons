minimum = 0
N = 1
R = 1
while R != 120 and R <= 120:
    R = bin(N)[2:]
    if N % 3 == 0:
        R += R[-3:]
    else:
        R += bin(N % 3 * 3)[2:]
    R = int(R, 2)
    N += 1
print(N - 1)