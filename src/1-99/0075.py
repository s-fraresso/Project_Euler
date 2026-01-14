from math import isqrt, ceil

lengths_triples_dict = dict()
UPPER_BOUND = 1_500_000

for p in range(2, isqrt(UPPER_BOUND)):
    for q in range(1, min(p, ceil(UPPER_BOUND/(2 * p) - p))):
        a = p**2 - q**2
        b = 2 * p * q
        c = p**2 + q**2
        a2, b2, c2 = (a, b, c)
        k = 1
        while a2 + b2 + c2 < UPPER_BOUND:
            triple = frozenset({a2, b2, c2})
            length = a2 + b2 + c2
            if length in lengths_triples_dict:
                matching_triples = lengths_triples_dict[length]
                matching_triples.add(triple)
            else:
                lengths_triples_dict[length] = {triple}
            k += 1
            a2 = k * a
            b2 = k * b
            c2 = k * c
        

print(sum(len(matching_triples) == 1 for matching_triples in lengths_triples_dict.values()))