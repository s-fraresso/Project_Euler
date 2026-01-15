def count_ways_to_fill(nb_tiles, min_block_size, memo):
    if nb_tiles < min_block_size:
        return 1
    
    if nb_tiles in memo:
        return memo[nb_tiles]
    
    nb_ways_to_fill = count_ways_to_fill(nb_tiles - 1, min_block_size, memo) # add 1 grey tile
    for block_size in range(min_block_size, nb_tiles + 1): # add a red block
        nb_ways_to_fill += count_ways_to_fill(nb_tiles - (block_size + 1), min_block_size, memo) # + 1 for the grey tile following the block
    
    memo[nb_tiles] = nb_ways_to_fill
    return nb_ways_to_fill


MIN_BLOCK_SIZE = 50
row_size = 50
while count_ways_to_fill(row_size, MIN_BLOCK_SIZE, {}) < 1_000_000:
    row_size += 1
print(row_size)