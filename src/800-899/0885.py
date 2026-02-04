from collections import Counter
from math import factorial

MOD = 1123455689


def count_ways_to_unsort(sorted_number, total_digit=18):
    c = Counter(map(int, str(sorted_number)))
    nb_ways = factorial(total_digit)
    for digit in c:
        nb_ways //= factorial(c[digit])
    nb_ways //= factorial(total_digit - len(str(sorted_number)))
    return nb_ways % MOD


def build_sorted_numbers(nb_digit, min_digit, current_number=0):
    global total
    if nb_digit == 0:
        total += (count_ways_to_unsort(current_number) * current_number) % MOD
        return
    
    for next_digit in range(min_digit, 10):
        build_sorted_numbers(nb_digit - 1, next_digit, current_number * 10 + next_digit)


total = 0
for nb_digit in range(1, 19):
    build_sorted_numbers(nb_digit, 1)
print(total % MOD)