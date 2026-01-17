from sympy import primerange

UPPER_BOUND = 10**9
PRIMES = list(primerange(101))

def count_hamming_numbers(largest_factor_index, smallest_factor_index=0, current_product=1):
    nb_hamming_numbers = 1 # current prime
    for i in range(smallest_factor_index, largest_factor_index + 1):
        new_product = current_product * PRIMES[i]
        if new_product > UPPER_BOUND:
            break
        nb_hamming_numbers += count_hamming_numbers(largest_factor_index, i, new_product)
    return nb_hamming_numbers


print(count_hamming_numbers(len(PRIMES) - 1))