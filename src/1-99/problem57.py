from fractions import Fraction

expansion = Fraction(1)
total = 0
for _ in range(1_000):
    expansion = 1 + (1 / (2 + (expansion - 1)))
    if len(str(expansion.numerator)) > len(str(expansion.denominator)):
        total += 1
print(total)