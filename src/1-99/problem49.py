from sympy import primerange, sieve
from collections import Counter

valid_sequences = []
for first in primerange(1_000, 10_000):
    for second in primerange(first + 1, 10_000):
        if Counter(str(first)) != Counter(str(second)):
            continue
        third = second + second - first
        if Counter(str(third)) == Counter(str(second)) and third in sieve:
            valid_sequences.append((first, second, third))
print(valid_sequences)