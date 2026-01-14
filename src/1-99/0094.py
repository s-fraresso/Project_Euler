from math import isqrt

"""
If a is the side length of the two equal sides, then the height h of the triangle
is given by the formula h = sqrt(a² - (a +- 1)²/4) thus we need to find a such that 
a² - (a +- 1)²/4 is a perfect square, this leads us to the OEIS sequence A120893.
This gives us the formula to iteratively compute the values of a, we then only 
need to check whether it's + or -.
"""

perimeter_sum = 0
a, b, c = 5, 1, 1

while 3 * a < 1_000_000_000:
    for base in ((a - 1), (a + 1)):
        h = isqrt(a**2 - (base // 2)**2)
        if h**2 + (base // 2)**2 == a**2:
            perimeter_sum += 2 * a + base
            
    a, b, c = 3 * a  + 3 * b - c, a, b

print(perimeter_sum)