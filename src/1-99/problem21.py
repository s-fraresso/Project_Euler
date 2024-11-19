from sympy import divisors

def sum_amicable_up_to(n):
    amicables = []
    for a in range(1, n):
        if a not in amicables:
            d_a = sum(divisors(a, True)) - a
            if a == d_a:
                continue
            d_b = sum(divisors(d_a, True)) - d_a
            if d_b == a:
                amicables.extend([a, d_a])
    return sum(amicables)


print(sum_amicable_up_to(10_000))