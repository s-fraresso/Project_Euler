from math import isqrt

def is_perfect_square(n):
    return isqrt(n)**2 == n

UPPER_BOUND = 100000

for z in range(1, UPPER_BOUND):
    for y in range(z + 1, UPPER_BOUND):
        if not is_perfect_square(y - z) or not is_perfect_square(y + z):
            continue
        for x in range(y + 1, UPPER_BOUND):
            if is_perfect_square(x + z) and is_perfect_square(x - z) and is_perfect_square(x + y) and is_perfect_square(x - y):
                print(x, y, z, x + y + z)