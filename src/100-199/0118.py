from itertools import permutations
from sympy.ntheory.primetest import isprime

valid_primes_dict = dict()
valid_primes = set()


for nb_digits in range(1, 9):
    for digits in permutations(range(1, 10), nb_digits):
        p = int(''.join(map(str, digits)))
        if isprime(p):
            key = frozenset(digits)
            if key in valid_primes_dict:
                valid_primes_dict[key].add(p)
            else:
                valid_primes_dict[key] = {p}
            valid_primes.add(p)

print(len(valid_primes))