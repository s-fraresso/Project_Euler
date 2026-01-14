MAX_N = 100_000

radicals = [1]*(MAX_N + 1)
for p in range(2, MAX_N):
    if radicals[p] != 1:
        continue
    for k in range(1, MAX_N // p + 1):
        radicals[k * p] *= p

print(sorted(list(range(MAX_N + 1)), key=lambda n: (radicals[n], n))[10_000])

