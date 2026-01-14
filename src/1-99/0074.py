from math import factorial


CYCLING_NUMBERS_DICT = {
    169:3, 363_601:3, 1454:3,
    871:2, 45_361:2,
    872:2, 45_362:2
}


def sum_digit_factorial(n):
    if n < 10:
        return factorial(n)
    return factorial(n % 10)  + sum_digit_factorial(n // 10)


def compute_non_repeating_chain_length(n):
    length = 0
    while n not in CYCLING_NUMBERS_DICT:
        length += 1
        next_n = sum_digit_factorial(n)
        if next_n == n:
            break
        n = next_n
    if n in CYCLING_NUMBERS_DICT:
        length += CYCLING_NUMBERS_DICT[n]
    return length


count = 0
for n in range(1, 1_000_000):
    if compute_non_repeating_chain_length(n) == 60:
        count += 1
    
print(count)
