from fractions import Fraction

# searching for curious fractions of the form ab / cd

curious_fractions = []

for a in range(1, 10):
    for b in range(10):
        for c in range(a, 10):
            for d in range(1, 10):
                if a != d and b != c:
                    continue
                frac = Fraction((a * 10 + b), (c * 10 + d))
                if frac >= 1:
                    continue
                if (a == d and frac == Fraction(b, c)) or (b == c and frac == Fraction(a, d)):
                    curious_fractions.append((frac))

product = 1
for frac in curious_fractions:
    product *= frac
print(product.denominator)