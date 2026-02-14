from sympy import nextprime, prime

"""
Using the binomial formula and merging the sum we get that
(p_n + 1)^n + (p_n - 1)^n = sum_{k=0}^n comb(k, n) p_n^k (1 + (-1)^(n - k))
taking mod p_n², we only need to account for the terms where k < 2 so the sum is
2 if n is even and 2 * n * p_n if n is odd so we only need to check for odd values of n
"""

n = 7037 # first n where 2*n*p_n > 10**9
p = prime(n)
while 2 * n * p <= 10**10:
    n += 2
    p = nextprime(p, 2)
print(n)