from sympy import divisor_count
from sympy.ntheory.generate import primorial

n = primorial(12)
step = n
while divisor_count(n**2) // 2 + 1 <= 4_000_000:
    n += step
print(n)