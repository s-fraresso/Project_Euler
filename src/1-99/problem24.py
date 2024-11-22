from math import factorial

def find_nth_permutation(values, n):
    n -= 1
    to_add = sorted(list(values))
    perm = []
    while to_add:
        p = factorial(len(to_add) - 1)
        perm.append(to_add.pop(n // p))
        n %= p
    return ''.join(map(str, perm))

print(find_nth_permutation(range(10), 1_000_000)) # 2783915460