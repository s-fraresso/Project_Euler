def p(n, memo={}):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif n in memo:
        return memo[n]
    
    nb_partitions = 0
    k = 1
    next_term = None
    while next_term != 0:
        next_term = (-1)**(k + 1) * (p(n - k * (3*k - 1) / 2) + p(n - k * (3 * k  +1) / 2))
        nb_partitions += next_term
        k += 1

    memo[n] = nb_partitions
    return nb_partitions


n = 0
while p(n) % 1_000_000 != 0:
    n += 1
print(n)
