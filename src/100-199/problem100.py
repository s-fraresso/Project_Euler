from math import isqrt

"""
the probability of getting two blue disks is b(b-1) / n(n-1) 
where b is the number of blue disks and n the total number of disks.
Solving for b > 0 gives b = (1 + sqrt(1 + 2 * n (n - 1))) / 2
since b needs to be an integer we need 1 + 2n(n-1) to be a perfect square.
solving for n > 0 : 1 + 2n(n-1) = r² => n = (1 + sqrt(2r² - 1)) / 2
thus we need to find r such that 2r² - 1 is a perfect square, such numbers 
are compiled in the A001653 sequence of the OEIS which gives us the formula 
a_(n+2) = 6a_(n+1) - a_n that we use to find the first valid root that yields
a value of n larger than 10^12 which we can check by solving for r
(1 + sqrt(2r² - 1)) / 2 >= 10^12. No need to test for parity at any point
since the numerators are always even.
"""

MIN_NB_DISKS = 10**12
MIN_ROOT = isqrt(((2 * MIN_NB_DISKS - 1)**2 + 1) // 2)

prev_root, root = 1, 5
while root < MIN_ROOT:
    root, prev_root = 6 * root - prev_root, root

nb_disks = (1 + isqrt(2 * root**2 - 1)) // 2
nb_blue_disks = (1 + isqrt(1 + 2 * nb_disks * (nb_disks - 1))) // 2
print(nb_blue_disks)