def sum_spiral_diagonal(size):
    return 1 + sum(4 * i**2 - 6 * (i - 1) for i in range(3, size + 1, 2))

print(sum_spiral_diagonal(1_001)) # 669171001