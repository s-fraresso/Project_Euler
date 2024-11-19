from math import log, floor, sqrt
from sympy import sieve
from sympy.ntheory import factorint

def count_prime_in_factorial(m, p):
    total = 0
    a = floor(log(m, p))
    for k in range(1, a + 1):
        total += m // p**k
    return total

def smallest_factorial_with_k_p(p, k):
    m = p
    while count_prime_in_factorial(m, p) < k:
        m += p
    return m

def s(n):
    return max(prime_power_dict[p][k] for (p, k) in prime_factorizations_list[n].items())

def S(N):
    return sum(s(n) for n in range(2, N + 1))

def build_prime_power_dict(limit):
    d = {p: dict() for p in sieve.primerange(limit)}
    cutoff = floor(sqrt(limit)) + 1
    for p in d:
        if p > cutoff:
            d[p][1] = p
        else:
            k = 1
            while p**k <= limit:
                d[p][k] = smallest_factorial_with_k_p(p, k)
                k += 1
    return d

def sieve_prime_factorizations(n):
    # Create a list to store the prime factorizations
    factors = [None] * (n + 1)
    
    # For each number, if it's still marked None, it's a prime
    for i in range(2, n + 1):
        if factors[i] is None:  # i is prime
            factors[i] = {i: 1}  # The prime factorization of a prime is {prime: 1}
            for j in range(2 * i, n + 1, i):
                if factors[j] is None:
                    factors[j] = {}
                # Count the power of prime i in j
                count = 0
                num = j
                while num % i == 0:
                    num //= i
                    count += 1
                if i in factors[j]:
                    factors[j][i] += count
                else:
                    factors[j][i] = count
    return factors


print("début")
prime_power_dict = build_prime_power_dict(100_000_000)
prime_factorizations_list = sieve_prime_factorizations(100_000_000)
print("dictionnaire des puissances premières générés")
print(S(100_000_000))
print("fin")