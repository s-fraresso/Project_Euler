for x in (2, 3, 5, 6, 7, 8, 10, 11, 12, 13):
    X = x**(1/2)
    a = []

    for _ in range(10):
        A = int(X)
        a.append(A)
        X = 1 / (X - A)

    print(x, a)