def power_digit_sum(n):
    string = str(2**n)
    total = 0
    for c in string:
        total += int(c)
    return total

print(power_digit_sum(1000))