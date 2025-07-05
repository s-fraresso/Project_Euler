def generate_pentagonal_numbers(n):
    return [k * (3*k - 1) // 2 for k in range(1, n + 1)]


pent_num = generate_pentagonal_numbers(100_000)
pent_num_set = set(pent_num)
D = float("+inf")
for k in range(2, 5_000):
    for j in range(1, k):
        if pent_num[k] + pent_num[j] in pent_num_set and \
        pent_num[k] - pent_num[j] in pent_num_set:
            D = min(D, pent_num[k] - pent_num[j])
print(D)