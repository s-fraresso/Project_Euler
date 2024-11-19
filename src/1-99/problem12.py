from sympy.ntheory import factorint

def count_divisors(n):
    factorization = factorint(n)
    nb_divisors = 1
    for power in factorization.values():
        nb_divisors *= power + 1
    return nb_divisors


def triangular_divisors(nb_divisor):
    n = 1
    i = 2
    while count_divisors(n) <= nb_divisor:
        n += i
        i += 1
    return n

print(triangular_divisors(500))