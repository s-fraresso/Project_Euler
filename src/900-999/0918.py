def a(n, memo={1:1}):
    if n in memo:
        return memo[n]

    memo[n] = 2 * a(n // 2) if n % 2 == 0 else a(n // 2) - 3 * a(n // 2 + 1)
    return memo[n]


print(4 - a(5 * 10**11))