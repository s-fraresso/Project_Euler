from sympy import divisors, totient, isprime


def A(n): # From problem 129
    if n % 3 == 0:
        n *= 9
    for k in divisors(totient(n)):
        if pow(10, k, n) == 1:
            return k


valid_composites = []
n = 9
while len(valid_composites) < 25:
    if (n - 1) % A(n) == 0:
        valid_composites.append(n)
    n += 1
    while n % 2 == 0 or n % 5 == 0 or isprime(n):
        n += 1
print(sum(valid_composites))