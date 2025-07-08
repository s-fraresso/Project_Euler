from sympy.ntheory import isprime

n = 9
increment = 2
nb_prime = 3
while nb_prime / (1 + (increment // 2) * 4) >= 0.1:
    increment += 2
    for i in range(1, 5):
        n += increment
        if isprime(n):
            nb_prime += 1
print(increment + 1)
