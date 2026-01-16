from sympy import primerange

def is_square_free(n):
    for p in primerange(int(n**(1/2)) + 1):
        if n % p**2 == 0:
            return False
    return True

current_row = [1]
square_free_numbers = {1}

for row_index in range(2, 52):
    new_row = [1]
    for i in range(len(current_row) - 1):
        new_term = current_row[i] + current_row[i + 1]
        new_row.append(new_term)
        if is_square_free(new_term):
            square_free_numbers.add(new_term)
    if row_index % 2 == 1:
        new_row.append(2 * current_row[-1])
        if is_square_free(2 * current_row[-1]):
            square_free_numbers.add(2 * current_row[-1])
    current_row = new_row

print(sum(square_free_numbers))