from math import log, sqrt, exp


def fib(n):
    a = b = 1
    k = 1
    while k < n:
        a, b = a + b, a
        k += 1
    return b


def is_fib_bipandigital(last_digits, k):
    return False


k = 2
fk, fprev = 1, 1 # first 9 digits of k-th fibonacci number
while not is_fib_bipandigital(fk, k):
    k += 1
    fk, fprev = (fk + fprev) % 10**9, fk


phi = (1 + sqrt(5)) / 2
n = 10
a = n * log(phi) - log(5) / 2
print(n, a, fib(n), exp(a))