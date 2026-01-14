m, n = 166, 144 # starting P_165 and H_143
pentagon = 41251 # No need to check for triangular numbers because all hexagonal numbers are triangular
hexagon = 41328

while pentagon != hexagon:
    mininum = min(pentagon, hexagon)
    if mininum == pentagon:
        pentagon += 3 * m + 1
        m += 1
    else:
        hexagon += 4 * n + 1
        n += 1

print(pentagon)