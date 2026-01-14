nb_valid_comb = 0
for n in range(1, 101):
    comb = 1
    r = 0
    while r <= n // 2 and comb <= 1_000_000:
        print(r, n, comb)
        nb_valid_comb += 2 if n % 2 == 1 or r != n // 2 else 1
        print("\t", nb_valid_comb)
        comb *= (n - r)
        comb //= (r + 1)
        r += 1
print((101 * 102) // 2 - 1 - nb_valid_comb)