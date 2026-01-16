MAX_TILES = 1_000_000
nb_laminae = 0

for full_square_side in range(3, (MAX_TILES // 4 + 1) + 1):
    hole_square_side = full_square_side - 2
    while hole_square_side > 0 and full_square_side**2 - hole_square_side**2 <= MAX_TILES:
        nb_laminae += 1
        hole_square_side -= 2

print(nb_laminae)