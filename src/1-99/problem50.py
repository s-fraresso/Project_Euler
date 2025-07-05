from sympy import primerange, sieve

primes = list(primerange(2, 1_000_000))

for nb_terms in range(547, 0, -1):
    print(nb_terms)
    s = sum(primes[:nb_terms])
    i = 0
    while s < 1_000_000 and s not in sieve and i < len(primes) - nb_terms:
        s -= primes[i]
        s += primes[nb_terms + i]
        i += 1
    if s in sieve:
        print(s, nb_terms, i)
        break