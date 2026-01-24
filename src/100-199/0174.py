"""
t is of type L(n) if there are n ways of writing t = a² - b² 
with a and b positive integers such that a - b >= 2 and a = b [2].
We get t = (a + b)(a - b), let x = a + b and y = a - b, t = xy
then, suppose t to be even (same reasoning for t odd),
x and y must both be even, so we write x = 2x' and y = 2y'
t = 4x'y', we get that t is a multiple of 4.
Now, we take t' = t / 4, x'y' = t', we need t' to have between 1 and 10 divisor pairs.
"""


total = 0
divisor_count = [2]*(250_000 + 1)

for n in range(2, 250_000 + 1):
    if 1 <= divisor_count[n] // 2 <= 10:
        total += 1

    m = 2 * n
    while m <= 250_000:
        divisor_count[m] += 1
        m += n

print(total)