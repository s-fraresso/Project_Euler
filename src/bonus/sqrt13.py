def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

NB_DIGIT = 1000

target_value = 13 * 10**(2 + NB_DIGIT * 2)
a = 0
b = 10**(NB_DIGIT + 3)

while a + 1 < b:
    m = (a + b) // 2
    if m**2 > target_value:
        b = m
    else:
        a = m

print(sum_digit(a) - 3 - (a % 10))