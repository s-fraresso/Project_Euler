from sympy import primerange

def S(p):
    total = 0
    prev = 1 # k = 2
    for k in range(2, 5):
        prev = (pow(p - k, -1, p) * prev) % p
        total += prev
    return total % p

print(sum(S(p) for p in primerange(5, 100_000_000 + 1)))