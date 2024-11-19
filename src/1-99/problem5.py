from functools import reduce
from sympy.ntheory import factorint

def smallest_multiple(n):
    smallest_factorization = {}
    for i in range(n, 1, -1):
        factorization = factorint(i)
        for factor in factorization:
            if factor in smallest_factorization:
                smallest_factorization[factor] = max(smallest_factorization[factor], factorization[factor])
            else:
                smallest_factorization[factor] = factorization[factor]
    return reduce(lambda env, factor: env * factor**smallest_factorization[factor], smallest_factorization, 1)

print(smallest_multiple(20))