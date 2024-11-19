from math import sqrt, floor

def largest_prime_factor(n):
    largest_factor = n

    for i in range(2, floor(sqrt(n)) + 1):
        while n % i == 0:
            largest_factor = i
            n //= i
    
    return largest_factor


print(largest_prime_factor(600851475143))