from sympy import divisors


def count_solutions(n):
    nb_solutions = 0
    for y in divisors(n): # (y + k)² - y² - (y - k)² = n <=> y(4k - y) = n
        k = (y + n // y) // 4
        if y - k > 0 and y * (4 * k - y) == n:
            nb_solutions += 1
    return nb_solutions


nb_ten_distinct_sol = 0
for n in range(1, 1_000_000):
    if count_solutions(n) == 10:
        nb_ten_distinct_sol += 1
print(nb_ten_distinct_sol)