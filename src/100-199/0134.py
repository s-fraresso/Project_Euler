from sympy import nextprime

def count_digits(n):
    nb_digits = 0
    while n > 0:
        nb_digits += 1
        n //= 10
    return nb_digits


def prime_pair_connection(p1, p2):
    p1_digit_length = count_digits(p1)
    inv = pow(p2, -1, 10**p1_digit_length)
    k = (p1 * inv) % 10**p1_digit_length
    return p2 * k


total = 0
p1, p2 = 5, 7
while p1 <= 1_000_000:
    total += prime_pair_connection(p1, p2)
    p1, p2 = p2, nextprime(p2)
print(total)