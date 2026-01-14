def int_to_list(n):
    return 

def nth_digit_product(limit):
    champernowne = []
    n = 0
    while len(champernowne) < 10**limit:
        champernowne.extend(int(digit) for digit in str(n))
        n += 1
    total = 1
    for i in range(limit):
        total *= champernowne[10**i]
    return total

print(nth_digit_product(6)) # 210