from math import log10, floor, log2

def p(L, n):
    k = 1 + floor(log10(L))
    nb_prefix_seen = 0
    power = 1 + floor((k - 1) * log2(10))
    while nb_prefix_seen < n:
        d = 1 + floor(power * log10(2))
        prefix = floor(10**(power * log10(2) - d + k))
        if prefix == L:
            nb_prefix_seen += 1
        power += 1
    return power - 1


print(p(123, 678910))