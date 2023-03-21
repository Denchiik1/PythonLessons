for n in range(2_000_000, 3_000_000):
    razn = []
    count = 0
    for delit in range(1, int(n ** 0.5) + 1):
        if n % delit == 0:
            x = delit
            y = n // delit
            d = abs(x - y)
            if x <= y and d <= 115:
                razn.append(d)
                count += 1
    if count > 2:
        print(n)