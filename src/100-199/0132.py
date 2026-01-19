from sympy import divisors, totient, nextprime


def A(p): # from problem 129
    for k in divisors(totient(p)):
        if pow(10, k, p) == 1:
            return k
        

p = 7
prime_factors = []
while len(prime_factors) < 40:
    if 10**9 % A(p) == 0:
        prime_factors.append(p)
    p = nextprime(p)
print(sum(prime_factors))