from math import comb

def lattice_paths(n):
    return comb(2 * n, n)

print(lattice_paths(20))