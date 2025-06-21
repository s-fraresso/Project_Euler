def sum_digit_power(n, power):
    if n < 10:
        return n**power
    return (n % 10)**power + sum_digit_power(n // 10, power)

def digit_n_power(n):
    valid = []
    for k in range(10**(n + 2)):
        if k == sum_digit_power(k, n):
            valid.append(k)
    print(valid)
    return valid

print(sum(digit_n_power(5)) - 1) # 443839