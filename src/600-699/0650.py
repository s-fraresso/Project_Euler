def merge_factorizations(base_facto, added_facto):
    for factor in added_facto:
        if factor in base_facto:
            base_facto[factor] += added_facto[factor]
        else:
            base_facto[factor] = added_facto[factor]


def exponentiate_factorization(facto, power):
    for factor in facto:
        facto[factor] *= power


MODULO = 1_000_000_007
UPPER_BOUND = 20_000
prime_factorization = [dict() for _ in range(UPPER_BOUND + 1)]
factorial_prime_factorization = [dict() for _ in range(UPPER_BOUND + 1)]
binom_prime_factorization = [dict() for _ in range(UPPER_BOUND + 1)]


for n in range(2, UPPER_BOUND + 1):
    if not prime_factorization[n]:
        power = 1
        base = n
        while base <= UPPER_BOUND:
            multiple = base
            k = 1
            while multiple <= UPPER_BOUND:
                if k % n != 0:
                    prime_factorization[multiple][n] = power
                multiple += base
                k += 1
            base *= n
            power += 1
    
    factorial_prime_factorization[n] = factorial_prime_factorization[n - 1].copy()
    merge_factorizations(factorial_prime_factorization[n], prime_factorization[n])

    binom_prime_factorization[n] = binom_prime_factorization[n - 1].copy()
    temp = prime_factorization[n].copy()
    exponentiate_factorization(temp, n - 1)
    merge_factorizations(binom_prime_factorization[n], temp)
    for factor, power in factorial_prime_factorization[n - 1].items():
        binom_prime_factorization[n][factor] -= power
        if binom_prime_factorization[n][factor] == 0:
            binom_prime_factorization[n].pop(factor)


def divisor_sum(factorization):
    sigma = 1
    for factor, power in factorization.items():
        sigma *= pow(factor, power + 1, MODULO) - 1
        sigma *= pow(factor - 1, -1, MODULO)
        sigma %= MODULO
    return sigma % MODULO


def D(n):
    return divisor_sum(binom_prime_factorization[n])


def S(n):
    return sum(D(k) % MODULO for k in range(1, n + 1)) % MODULO


print(S(20_000))