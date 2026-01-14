from sympy import sieve, nextprime


def is_truncatable_prime_rec(p, is_left_to_right):
    if p < 10:
        return p in sieve
    next_p = int(str(p)[1:]) if is_left_to_right else int(str(p)[:-1])
    return p in sieve and is_truncatable_prime_rec(next_p, is_left_to_right)


def is_truncatable_prime(p):
    return is_truncatable_prime_rec(p, True) and is_truncatable_prime_rec(p, False)


truncatable_primes = []
p = 11
while len(truncatable_primes) < 11:
    if is_truncatable_prime(p):
        truncatable_primes.append(p)
    p = nextprime(p)

print(sum(truncatable_primes))