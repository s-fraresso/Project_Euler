from sympy import divisors, totient, primerange


def is_only_multiple_of(n, divs):
    for div in divs:
        while n > 1 and n % div == 0:
            n //= div
    return n == 1


def A(n):
    if n % 3 == 0:
        n *= 9
    for k in divisors(totient(n)):
        if pow(10, k, n) == 1:
            return k
        

prime_sum = 2 + 3 + 5
for p in primerange(7, 100_000):
    if not is_only_multiple_of(A(p), (2, 5)):
        prime_sum += p
print(prime_sum)