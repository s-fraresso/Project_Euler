def count_ways_to_make(goal_amount, available_coins, memo=dict()):
    if (goal_amount, tuple(available_coins)) in memo:
        return memo[(goal_amount, tuple(available_coins))]
    
    if goal_amount == 0 or len(available_coins) <= 1:
        return 1
    
    res = 0
    for i in range(len(available_coins)):
        if available_coins[i] <= goal_amount:
            res += count_ways_to_make(goal_amount - available_coins[i], available_coins[:i+1])

    memo[(goal_amount, tuple(available_coins))] = res
    return res


print(count_ways_to_make(200, [200, 100, 50, 20, 10, 5, 2, 1]))