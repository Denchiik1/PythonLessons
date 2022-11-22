mas = [1, 2, 2, 3]
j = mas[0]
for i in range(1, len(mas)):
    if i > j:
        j = mas[i]
print(j)