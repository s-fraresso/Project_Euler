from decimal import *

getcontext().prec = 100
PI = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286')


def distance_to_nearest_integer(x):
    return abs(x - round(x))


def cosh(x):
    return (x.exp() + (-x).exp()) / 2


min_dist = float("+inf")
best_n = 0
for n in range(1, 1001):
    dist = distance_to_nearest_integer(cosh(PI * Decimal(n).sqrt()))
    if dist < min_dist:
        min_dist = dist
        best_n = -n
print(best_n)


"""
On vérifie dans un premier temps que 962 (31^2 + 1) n'est pas la solution,
on cherche donc une solution négative, sachant que cos(ix) = cosh(x)
on utilise le module Decimal car la précision des float n'est pas suffisante
"""