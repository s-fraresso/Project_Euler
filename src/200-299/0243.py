from sympy.functions.combinatorial.numbers import totient
from sympy.ntheory.generate import primorial


UPPER_BOUND = 15_499 / 94_744
d = primorial(9)
step = d
while totient(d) / (d - 1) >= UPPER_BOUND:
    d += step
print(d)