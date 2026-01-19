from sympy import divisors, totient


def A(n):
    if n % 3 == 0:
        n *= 9
    for k in divisors(totient(n)):
        if pow(10, k, n) == 1:
            return k


n = 1_000_001 # A(n) <= n
while A(n) <= 1_000_000:
    n += 1
    while n % 2 == 0 or n % 5 == 0:
        n += 1
print(n)