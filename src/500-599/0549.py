def sieve(limit):
    smallest_factorial = [0]*(limit + 1)

    for n in range(2, limit + 1):
        if smallest_factorial[n] == 0:
            power = n
            m = n
            while power <= limit:
                for multiple in range(power, limit + 1, power):
                    smallest_factorial[multiple] = max(m, smallest_factorial[multiple])

                iterated_quotient = m // n
                while iterated_quotient % n == 0:
                    power *= n
                    iterated_quotient //= n
                power *= n
                m += n

    return sum(smallest_factorial)


print(sieve(100_000_000)) # 476001479068717
