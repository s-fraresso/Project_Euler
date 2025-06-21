from sympy import sieve

def is_goldbach_number(n, double_squares):
    for p in sieve:
        if p >= n:
            break
        for sq in double_squares:
            if sq + p > n:
                break
            if sq + p == n:
                return True
    return False

def goldbach_counter():
    double_squares = [2 * i**2 for i in range(1, 1_000)]
    n = 9
    while is_goldbach_number(n, double_squares):
        n += 2
        while n in sieve:
            n += 2
    return n

print(goldbach_counter()) # 5777