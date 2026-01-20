def count_valid_numbers(nb_digit, prev_digit, second_prev_digit, memo={}):
    key = (nb_digit, prev_digit, second_prev_digit)
    if key in memo:
        return memo[key]

    if nb_digit == 1:
        return 10 - prev_digit - second_prev_digit
    
    nb_valid_numbers = 0
    for next_digit in range(10 - prev_digit - second_prev_digit):
        nb_valid_numbers += count_valid_numbers(nb_digit - 1, next_digit, prev_digit, memo)
    memo[key] = nb_valid_numbers
    return nb_valid_numbers


total_valid = 0
for first_digit in range(1, 10):
    for second_digit in range(10 - first_digit):
        total_valid += count_valid_numbers(18, second_digit, first_digit)
print(total_valid)