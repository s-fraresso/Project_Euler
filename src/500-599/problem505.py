from math import floor

memo = {"x": {0:0, 1:1, 2:3, 3:2, 4:11}, "y": {(4, 4):11, (4, 3):2**60 - 9, (4, 2):2**60 - 12, (4, 1):8}, "A": {4:8, 10:2**60 - 34, 1_000:101881}}

def x(n):
    if n not in memo["x"]:
        k = n // 2
        memo["x"][n] = (3 * x(k) + 2 * x(k // 2)) % (2**60) if n % 2 == 0 else 2 * x(k) + 3 * x(k // 2) % (2**60)
    return memo["x"][n]

def y(n, k):
    if (n, k) not in memo["y"]:
        memo["y"][(n, k)] = x(k) if k >= n else 2**60 - 1 - max(y(n, 2*k), y(n, 2*k + 1))
    return memo["y"][(n, k)]

def A(n):
    if n not in memo["A"]:
        memo["A"][n] = y(n, 1)
    return memo["A"][n]


print(A(1_000_000_000_000)) # Too slow
