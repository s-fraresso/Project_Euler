from sympy import sieve

def prime_until(a, b):
    n = 0
    while n**2 + a*n + b in sieve:
        n += 1
    return n

def max_prime_polynomial(a_max, b_max):
    max_prime_generated = 0
    best_a = 0
    best_b = 0
    for a in range(-a_max + ((a_max + 1) % 2), a_max + 1, 2):
        for b in sieve.primerange(b_max + 1):
            for b_sign in (-1, 1):
                p = prime_until(a, b_sign * b)   
                if p > max_prime_generated:
                    max_prime_generated = p
                    best_a = a
                    best_b = b * b_sign
    return (best_a, best_b)

def quadratic_primes(limit):
    a, b = max_prime_polynomial(limit, limit)
    return a * b

print(quadratic_primes(1000)) # -59231