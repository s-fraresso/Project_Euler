from sympy import sieve, totient, factorint
from collections import Counter


def is_permutation(a, b):
    return Counter(str(a)) == Counter(str(b))


min_ratio = float("+inf")
best_n = -1
n = 10**6
for phi in sieve.totientrange(10**6, 10**7):
    if is_permutation(n, phi) and n / phi < min_ratio:
        min_ratio = n / phi
        best_n = n
    n += 1
print(best_n)