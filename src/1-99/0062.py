def get_digits_counts(number):
    digits_counts = [0]*10
    for digit in str(number):
        digits_counts[int(digit)] += 1
    return tuple(digits_counts)


nb_cubes_per_digits = dict()
for n in range(10_000):
    cube = n**3
    digits_counts = get_digits_counts(cube)

    if digits_counts not in nb_cubes_per_digits:
        nb_cubes_per_digits[digits_counts] = [1, n]
    else:
        nb_cubes_per_digits[digits_counts][0] += 1
        if nb_cubes_per_digits[digits_counts][0] >= 5:
            print(nb_cubes_per_digits[digits_counts][1]**3)
            break