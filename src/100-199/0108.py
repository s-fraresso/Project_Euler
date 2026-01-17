from sympy import divisors

def count_solutions(n):
    solution_pairs = set()
    for d in divisors(n**2):
        y = d + n
        x = n + (n**2 // d)
        solution_pairs.add(frozenset({x, y}))
    return len(solution_pairs)


n = 2 * 3 * 5 * 7 * 11 * 13
step = n
while count_solutions(n) <= 1_000:
    n += step
print(n)