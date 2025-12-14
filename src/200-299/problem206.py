def get_ith_digit(n, i):
    return (n % 10**(i+1)) // (10**i)


for root in range(int(round((1020304050607080900)**(1/2), -1)), int((1929394959697989990)**(1/2)) + 1, 10):
    n = root**2
    is_valid = True
    for i, digit in enumerate(range(9, 0, -1)):
        if get_ith_digit(n,  2 + 2 * i) != digit:
            is_valid = False
            break
    if is_valid:
        break

print(root)