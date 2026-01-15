def ways_to_tile(nb_tiles, block_size, memo):
    if nb_tiles in memo:
        return memo[nb_tiles]

    if nb_tiles < block_size:
        return 1
    
    nb_ways = ways_to_tile(nb_tiles - block_size, block_size, memo) + ways_to_tile(nb_tiles - 1, block_size, memo)
    memo[nb_tiles] = nb_ways
    return nb_ways

print(ways_to_tile(50, 2, {}) + ways_to_tile(50, 3, {}) + ways_to_tile(50, 4, {}) - 3) # not counting the all grey tilings
