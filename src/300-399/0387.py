from sympy import isprime


def digit_sum(n):
    return sum(map(int, str(n)))


def is_harshad_number(n):
    return n % digit_sum(n) == 0


UPPER_BOUND = 10**14
strong_right_truncatable_harshad_primes_sum = 0
harshad_numbers = list(range(1, 10))

while harshad_numbers:
    n = harshad_numbers.pop(0)
    
    for next_digit in range(10): # builds new harshad numbers / strong harshad primes iteratively
        augmented_n = 10 * n + next_digit

        if augmented_n >= UPPER_BOUND:
            break
        if isprime(augmented_n) and isprime(n // digit_sum(n)): # augmented_n is a strong truncatable harshad prime
            strong_right_truncatable_harshad_primes_sum += augmented_n
        elif is_harshad_number(augmented_n):
            harshad_numbers.append(augmented_n)

print(strong_right_truncatable_harshad_primes_sum)