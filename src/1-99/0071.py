from fractions import *

def find_left_fraction(d, reference):
    leftmost_fraction = Fraction(0)
    for denominator in range(2, d + 1):
        f = Fraction(denominator * reference.numerator // reference.denominator, denominator)
        if f > leftmost_fraction and f != reference:
            leftmost_fraction = f
    return leftmost_fraction

print(find_left_fraction(1_000_000, Fraction(3, 7)).numerator) # 428570