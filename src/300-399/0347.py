from sympy import primerange


def S(N):
    max_products_of_two = set()

    for p in primerange(2, int(N**(1/2)) + 1):
        for q in primerange(p + 1, N // p + 1):
            max_prod = float("-inf")
            pa = p
            while pa * q <= N:
                prod = pa * q
                while prod <= N:
                    max_prod = max(max_prod, prod)
                    prod *= q
                pa *= p
            
            max_products_of_two.add(max_prod)

    return sum(max_products_of_two)


print(S(10_000_000))
