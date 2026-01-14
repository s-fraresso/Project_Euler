from bisect import insort


def read_matrix(input_file):
    cost_matrix = []
    with open(input_file, 'r') as f:
        for line in f:
            cost_matrix.append(list(map(int, line.split(','))))
    return cost_matrix


def min_path_sum(cost_matrix, start, end):
    min_cost_matrix = [[None]*len(cost_matrix[i]) for i in range(len(cost_matrix))]
    min_cost_matrix[start[0]][start[1]] = cost_matrix[start[0]][start[1]]
    processed_nodes = set()
    pending_nodes = [(cost_matrix[start[0]][start[1]], start[0], start[1])]

    i = j = None
    while pending_nodes and (i, j) != end:
        cost, i, j = pending_nodes.pop(0)

        if (i, j) in processed_nodes:
            continue

        min_cost_matrix[i][j] = cost

        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if 0 <= i2 < len(cost_matrix) and 0 <= j2 < len(cost_matrix[i2]) and (i2, j2) not in processed_nodes:
                insort(pending_nodes, (cost + cost_matrix[i2][j2], i2, j2))
        
        processed_nodes.add((i, j))

    return min_cost_matrix[end[0]][end[1]]

print(min_path_sum(read_matrix("input_files\\0083_matrix.txt"), (0, 0), (79, 79)))