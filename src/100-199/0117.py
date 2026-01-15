def ways_to_tile(nb_tiles, block_sizes, memo={}):
    if nb_tiles in memo:
        return memo[nb_tiles]

    if nb_tiles < min(block_sizes):
        return 1
    
    nb_ways = 0
    for size in block_sizes:
        if size > nb_tiles:
            continue

        nb_ways += ways_to_tile(nb_tiles - size, block_sizes, memo)

    memo[nb_tiles] = nb_ways
    return nb_ways

print(ways_to_tile(50, (1, 2, 3, 4)))