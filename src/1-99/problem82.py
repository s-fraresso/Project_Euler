def read_graph(input_file):
    cost = dict()
    with open(input_file, 'r') as f:
        i = 0
        for line in f:
            j = 0
            for coef in line.split(','):
                cost[(i, j)] = int(coef)
                j += 1
            i += 1
    return cost, i


def get_neighbours(s, N):
    x, y = s
    return ((i, j) for i, j in ((x + 1, y), (x - 1, y), (x, y + 1)) if 0 <= i < N and j < N)


def init_distances(cost, N):
    dist = {(i, j) : float("+inf") for i in range(N) for j in range(N)}
    for i in range(N):
        dist[(i, 0)] = cost[(i, 0)]
    return dist


def pop_next_vertex(to_process, processed, dist):
    vertex = min(to_process, key=lambda s: dist[s])
    to_process.remove(vertex)
    processed.add(vertex)
    return vertex


def min_path_sum(input_file):
    cost, N = read_graph(input_file)
    dist = init_distances(cost, N)
    processed = set()
    to_process = {(i, 0) for i in range(N)}
    while to_process:
        s1 = pop_next_vertex(to_process, processed, dist)
        if s1[1] == N - 1:
            break
        for s2 in get_neighbours(s1, N):
            if s2 not in processed:
                dist[s2] = min(dist[s2], dist[s1] + cost[s2])
                to_process.add(s2)
    return min(dist[(i, N - 1)] for i in range(N))


print(min_path_sum("input_files\\0081_matrix.txt"))