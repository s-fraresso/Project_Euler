from math import sqrt, floor

def sum_prime(threshold):
    total = 2
    primes = [2]
    k = 3
    while k < threshold:
        r = floor(sqrt(k)) + 1
        is_prime = True
        for p in primes:
            if p > r:
                break
            if k % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(k)
            total += k
        k += 2
    return total


print(sum_prime(10))
print(sum_prime(2_000_000))