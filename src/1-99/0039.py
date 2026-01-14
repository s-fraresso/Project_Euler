def nb_pythagorean_solutions(p):
    nb_solutions = 0
    for a in range(p // 2):
        for b in range(a, p // 2):
            if a**2 + b**2 == (p - a - b)**2:
                nb_solutions += 1
    return nb_solutions

def max_solutions(limit):
    best_p = -1
    max_sol = 0
    for p in range(4, limit + 1):
        sol = nb_pythagorean_solutions(p)
        if sol > max_sol:
            max_sol = sol
            best_p = p
    return best_p

print(max_solutions(1_000)) # 840