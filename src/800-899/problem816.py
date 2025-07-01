from math import sqrt, ceil


def rng_next(curr_val):
    return pow(curr_val, 2, 50_515_093)


def shortest_distance_in_batch(points):
    min_dist = float("+inf")
    for a in range(len(points) - 1):
        for b in range(a + 1, len(points)):
            x1, y1 = points[a]
            x2, y2 = points[b]
            dist = (x1 - x2)**2 + (y1 - y2)**2
            min_dist = min(dist, min_dist)
    return min_dist


def shortest_distance_in_grid(grid):
    min_dist = float("+inf")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            points = grid[i][j]
            if i < len(grid) - 1:
                points.extend(grid[i + 1][j])
                if j < len(grid[i]) - 1:
                    points.extend(grid[i + 1][j + 1])
            if j < len(grid[i]) - 1:
                points.extend(grid[i][j + 1])
            min_dist = min(min_dist, shortest_distance_in_batch(points))
    return min_dist


def shortest_distance(nb_points):
    nb_divs = int(sqrt(nb_points))
    div_length = ceil(50_515_093 / nb_divs)
    grid = [[[] for _ in range(nb_divs)] for _ in range(nb_divs)]
    next_x = 290_797
    next_y = rng_next(next_x)
    for k in range(nb_points):
        grid[next_x // div_length][next_y // div_length].append((next_x, next_y))
        next_x = rng_next(next_y)
        next_y = rng_next(next_x)
    return sqrt(shortest_distance_in_grid(grid))


print(round(shortest_distance(2_000_000), 9)) # 20.880613018