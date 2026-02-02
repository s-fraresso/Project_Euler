from sympy import nextprime, isprime
from math import isqrt


def reverse_integer(n):
    reverse = 0
    while n != 0:
        reverse *= 10
        reverse += n % 10
        n //= 10
    return reverse


reversible_prime_squares = []
p = 2
while len(reversible_prime_squares) < 50:
    p_sq = p * p
    reversed_p_sq = reverse_integer(p_sq)
    reversed_p = isqrt(reversed_p_sq)
    if reversed_p * reversed_p == reversed_p_sq and isprime(reversed_p) and reversed_p_sq != p_sq:
        reversible_prime_squares.append(p_sq)
    p = nextprime(p)

print(sum(reversible_prime_squares))