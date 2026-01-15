UPPER_BOUND = 10**8

prime_factor_count = [0]*(UPPER_BOUND)

for p in range(2, UPPER_BOUND):
    if prime_factor_count[p] != 0:
        continue
    power = 1
    divisor = p
    while divisor < UPPER_BOUND:
        k = 1
        while divisor * k < UPPER_BOUND:
            if k % p != 0:
                prime_factor_count[divisor * k] += power
            k += 1
        power += 1
        divisor *= p

print(prime_factor_count.count(2))