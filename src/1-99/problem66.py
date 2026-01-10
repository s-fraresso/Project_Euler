def compute_min_x(D):
    solution_found = False
    x = 2
    while not solution_found:
        if (x**2) % D != 1:
            x += 1
            continue

        target_square = (x**2 - 1) // D
        if (int(target_square**(1/2)))**2 == target_square:
            break
        x += 1
    return x


for D in range(100):
    if int(D**(1/2))**2 == D:
        continue
    print(D, compute_min_x(D))