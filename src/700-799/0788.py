from math import comb


def comb2(n, k, memo=dict()):
    if (n, k) not in memo:
        memo[(n, k)] = comb(n, k)

    return memo[(n, k)]


def count_dom(nb_digit):
    nb_dom = 0
    
    # dom digit != 0
    for nb_dom_digit in range(nb_digit // 2 + 1, nb_digit + 1):
        nb_dom += 9**(nb_digit - nb_dom_digit) * comb2(nb_digit - 1, nb_dom_digit - 1) # a dom digit goes in first place
        nb_dom += 8 * 9**max(0, (nb_digit - nb_dom_digit - 1)) * comb2(nb_digit - 1, nb_dom_digit) # a non dom digit goes in first place (so no 0 either)
    
    nb_dom *= 9 # for each possible dom digit != 0

    # dom digit = 0
    for nb_zero in range(nb_digit // 2 + 1, nb_digit):
        nb_dom += 9**(nb_digit - nb_zero) * comb2(nb_digit - 1, nb_zero)
    
    return nb_dom


def D(n):
    return sum(count_dom(nb_digit) % 1_000_000_007 for nb_digit in range(1, n + 1)) % 1_000_000_007


print(D(2022))