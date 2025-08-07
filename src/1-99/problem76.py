def ways_to_sum(n, max_add, memo={(0, 0):1}):
    if (n, max_add) in memo:
        return memo[n, max_add]
    
    total = 0
    for i in range(max_add, 0, -1):
        total += ways_to_sum(n - i, min(i, n - i))

    memo[(n, max_add)] = total
    return total


print(ways_to_sum(100, 99))

