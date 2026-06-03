from collections import Counter
from math import comb


def ref_D(N):
    nb_dom = 0

    for nb_digit in range(1, N + 1):
        for n in range(10**(nb_digit - 1), 10**nb_digit):
            if any(digit_count > nb_digit // 2 for digit_count in Counter(str(n)).values()):
                nb_dom += 1

    return nb_dom

print(ref_D(6) - ref_D(5))

# N = 4
nb_dom = 0
# dom digit = 0
nb_dom += 9 * 1
# dom digit != 0
nb_dom += 9 * (comb(4, 4) + comb(3, 2) * 9 + 8)
print(nb_dom)

# N = 5
nb_dom = 0
# dom digit = 0
nb_dom += 9**1 + 9**2 * comb(4, 3)
# dom_digit != 0
nb_dom += 9 * (comb(5, 5) +                             # 5
               comb(4, 3) * 9 + 8 +                     # 4
               comb(4, 2) * 9**2 + 8 * comb(4, 3) * 9)  # 3
print(nb_dom)

# N = 6
nb_dom = 0
# dom digit = 0
nb_dom += (9**1 +                                       # 5
           9**2 * comb(5, 4))                           # 4
# dom_digit != 0
nb_dom += 9 * (comb(6,6) +                              # 6
               comb(5, 4) * 9 + 8 +                     # 5
               comb(5, 3) * 9**2 + 8 * comb(5, 4) * 9)  # 4
print(nb_dom)