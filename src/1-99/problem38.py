def concatenated_product(n):
    concat = []
    k = 1
    while len(concat) < 9:
        concat.extend(list(str(n * k)))
        k += 1
    return concat


max_pandigital_number = -1
for n in range(1, 10_000):
    concat = concatenated_product(n)
    if sorted(concat) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        max_pandigital_number = max(max_pandigital_number, int(''.join(concat)))
print(max_pandigital_number)