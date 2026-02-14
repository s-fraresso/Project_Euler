from math import log, sqrt, exp


def fib(n):
    a = b = 1
    k = 1
    while k < n:
        a, b = a + b, a
        k += 1
    return b


phi = (1 + sqrt(5)) / 2
n = 10
a = n * log(phi) - log(5) / 2
print(n, a, fib(n), exp(a))