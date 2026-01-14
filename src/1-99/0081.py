def node_value(matrix, i, j, node_value_dict = {}):
    if (i, j) not in node_value_dict:
        if i < len(matrix) - 1 and j < len(matrix) - 1:
            node_value_dict[(i, j)] = matrix[i][j] + min(node_value(matrix, i + 1, j), node_value(matrix, i, j + 1))
        elif i < len(matrix) - 1:
            node_value_dict[(i, j)] = matrix[i][j] + node_value(matrix, i + 1, j)
        elif j < len(matrix) - 1:
            node_value_dict[(i, j)] = matrix[i][j] + node_value(matrix, i, j + 1)
        else:
            node_value_dict[(i, j)] = matrix[i][j]
    return node_value_dict[(i, j)]


def min_path_sum(input_file):
    matrix = []
    with open(input_file, 'r') as f:
        for line in f:
            matrix.append([int(coef) for coef in line.split(',')])
    return node_value(matrix, 0, 0)

print(min_path_sum("input_files\\0081_matrix.txt")) # 427337

