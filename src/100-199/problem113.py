def count_non_bouncy_numbers(nb_digits):
    total = 0
    increasing_memo, decreasing_memo = dict(), dict()
    for exact_nb_digits in range(1, nb_digits + 1):
        for starting_digit in range(1, 10):
            total += count_ordered_numbers(True, exact_nb_digits - 1, starting_digit, increasing_memo)
            total += count_ordered_numbers(False, exact_nb_digits - 1, starting_digit, decreasing_memo)
    total -= nb_digits * 9 # to compensate double counting of 1-9, 111-999, etc.
    return total


def count_ordered_numbers(is_increasing, nb_digits, limit_digit, memo):
    if (nb_digits, limit_digit) in memo:
        return memo[(nb_digits, limit_digit)]
    if nb_digits == 0:
        return 1
    res = 0
    digit_range = range(limit_digit, 10) if is_increasing else range(limit_digit + 1)
    for next_digit in digit_range:
        res += count_ordered_numbers(is_increasing, nb_digits - 1, next_digit, memo)
    memo[(nb_digits, limit_digit)] = res
    return res


nb_digits = 10
print(count_non_bouncy_numbers(nb_digits))
