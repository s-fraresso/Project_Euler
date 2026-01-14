from math import sqrt, floor

def nth_prime(n):
    primes = [2]
    k = 3
    while len(primes) < n:
        threshold = floor(sqrt(k)) + 1
        is_prime = True
        for p in primes:
            if p > threshold:
                break
            if k % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(k)
        k += 2
    return primes[-1]


print(nth_prime(10_001))
