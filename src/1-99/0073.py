from fractions import *

def count_reduced_proper_fractions_between(lower, upper, d):
    valid_fractions = set()
    for denominator in range(2, d + 1):
        for numerator in range(denominator * lower.numerator // lower.denominator + 1, denominator * upper.numerator // upper.denominator + 1):
            f = Fraction(numerator, denominator)
            valid_fractions.add(f)
    valid_fractions.discard(lower)
    valid_fractions.discard(upper)
    return len(valid_fractions)

print(count_reduced_proper_fractions_between(Fraction(1, 3), Fraction(1, 2), 12_000)) # 7295372
