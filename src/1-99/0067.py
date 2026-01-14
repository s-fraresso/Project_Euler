def node_value(triangle, i, j, node_value_dict = {}):
    if (i, j) in node_value_dict:
        return node_value_dict[(i, j)]
    
    node_value_dict[(i, j)] = triangle[i][j]
    if i < len(triangle) - 1:
        node_value_dict[(i, j)] += max(node_value(triangle, i + 1, j), node_value(triangle, i + 1, j + 1))
    return node_value_dict[(i, j)]


def maximum_path_sum(input_file):
    triangle = []
    with open(input_file, 'r') as f:
        for line in f:
            triangle.append([int(val) for val in line.split(' ')])
    return node_value(triangle, 0, 0)

print(maximum_path_sum("input_files\\0067_triangle.txt")) # 7273