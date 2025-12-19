def compute_max_square_remainder(a):
    alpha_remainders = set()
    beta_remainders = set()

    alpha_r = beta_r = 1 # alpha = (a - 1)^n ; beta = (a + 1)^n
    r_max = (alpha_r + beta_r) % a**2

    while not (alpha_r in alpha_remainders and beta_r in beta_remainders):
        alpha_remainders.add(alpha_r)
        beta_remainders.add(beta_r)
        
        alpha_r = (alpha_r * (a - 1)) % a**2
        beta_r = (beta_r * (a + 1)) % a**2
        r_max = max(r_max, (alpha_r + beta_r) % a**2)

    return r_max


print(sum(compute_max_square_remainder(a) for a in range(3, 1_000 + 1)))