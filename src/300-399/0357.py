from sympy import sieve, divisors


def is_prime_generating(n):
    for d in divisors(n, generator=True):
        if d + n // d not in sieve:
            return False
    return True


sum_prime_generating_integers = 0
for p in sieve.primerange(2, 100_000_000 + 1):
    if is_prime_generating(p - 1):
        sum_prime_generating_integers += (p - 1)

print(sum_prime_generating_integers)
