def square_digit(n, memo={0:0}):
    if n in memo:
        return memo[n]
    memo[n] = (n % 10)**2 + square_digit(n // 10)
    return memo[n]


def square_digit_chain_end(n, memo={1:1, 89:89}):
    if n in memo:
        return memo[n]
    memo[n] = square_digit_chain_end(square_digit(n))
    return memo[n]


total = 0
for n in range(1, 10_000_001):
    if square_digit_chain_end(n) == 89:
        total += 1
print(total)