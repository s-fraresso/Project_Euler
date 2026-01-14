collatz_dict = {1: 1}

def collatz_steps(n):
    if n not in collatz_dict:
        next_n = n // 2 if n % 2 == 0 else 3 * n + 1
        collatz_dict[n] = 1 + collatz_steps(next_n)
    return collatz_dict[n]


def longest_collatz(n):
    max_steps = float("-inf")
    best_start = 0
    for start in range(1, n):
        steps = collatz_steps(start)
        if steps > max_steps:
            max_steps = steps
            best_start = start
    return best_start

print(longest_collatz(1_000_000))
