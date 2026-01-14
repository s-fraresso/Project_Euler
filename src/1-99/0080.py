def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def square_root_digit_sum(n, nb_digits):
    nb_decimals = nb_digits - len(str(int(n**(1/2))))
    target_value = n * 10**(2 + nb_decimals * 2)
    a = 0
    b = 10**(nb_decimals + 3)

    while a + 1 < b:
        m = (a + b) // 2
        if m**2 > target_value:
            b = m
        else:
            a = m
    return sum_digit(a) - a % 10

total = 0
for n in range(100):
    if int(n**(1/2))**2 != n: # n isn't a perfect square
        total += square_root_digit_sum(n, 100)
print(total)
