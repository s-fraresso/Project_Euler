MIN_BLOCK_SIZE = 3


def count_ways_to_fill(nb_tiles, memo={}):
    if nb_tiles < MIN_BLOCK_SIZE:
        return 1
    
    if nb_tiles in memo:
        return memo[nb_tiles]
    
    nb_ways_to_fill = count_ways_to_fill(nb_tiles - 1, memo) # add 1 grey tile
    for block_size in range(MIN_BLOCK_SIZE, nb_tiles + 1): # add a red block
        nb_ways_to_fill += count_ways_to_fill(nb_tiles - (block_size + 1)) # + 1 for the grey tile following the block
    
    memo[nb_tiles] = nb_ways_to_fill
    return nb_ways_to_fill


print(count_ways_to_fill(50))