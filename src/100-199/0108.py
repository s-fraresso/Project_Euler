from sympy import divisor_count
from sympy.ntheory.generate import primorial


n = primorial(6)
step = n
while divisor_count(n**2) // 2 + 1 <= 1_000:
    n += step
print(n)