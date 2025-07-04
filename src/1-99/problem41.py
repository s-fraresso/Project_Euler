from sympy import sieve
from itertools import permutations

n = -1
is_answer_found = False
for nb_digit in range(7, 0, -1): # 8 and 9 pandigital numbers are always divisible by 3
    for pandigital_perm in permutations(range(nb_digit, 0, -1), nb_digit):
        n = int(''.join(map(str, pandigital_perm)))
        if n in sieve:
            is_answer_found = True
            break
    if is_answer_found:
        break
print(n)