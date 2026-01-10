def generate_4_digit_figurates(formula):
    n = 1
    P = formula(n)
    while P < 1000:
        n += 1
        P = formula(n)
    figurate_numbers = []

    while P < 10_000:
        figurate_numbers.append(P)
        n += 1
        P = formula(n)

    return tuple(figurate_numbers)


def build_cyclic_set(current_set, remaining_shapes):
    if len(remaining_shapes) == 0:
        if current_set[-1] % 100 == current_set[0] // 100:
            print(current_set)
    else:
        target_digits = current_set[-1] % 100
        for shape in remaining_shapes:
            i = 0
            while shape[i] < target_digits * 100:
                i += 1
            while shape[i] < (target_digits + 1) * 100:
                current_set.append(shape[i])
                build_cyclic_set(current_set, remaining_shapes.difference({shape}))
                current_set.pop()
                i += 1


TRIANGLE = generate_4_digit_figurates(lambda n: n * (n + 1) // 2)
SQUARE = generate_4_digit_figurates(lambda n: n**2)
PENTAGONAL = generate_4_digit_figurates(lambda n: n * (3*n - 1) // 2)
HEXAGONAL = generate_4_digit_figurates(lambda n: n * (2*n - 1))
HEPTAGONAL = generate_4_digit_figurates(lambda n: n * (5*n - 3) // 2)
OCTOGONAL = generate_4_digit_figurates(lambda n: n * (3*n - 2))

for tri in TRIANGLE:
    build_cyclic_set([tri], {SQUARE, PENTAGONAL, HEXAGONAL, HEPTAGONAL, OCTOGONAL})

print(8256 + 5625 + 2512 + 1281 + 8128 + 2882) # 28684