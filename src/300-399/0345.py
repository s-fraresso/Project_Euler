from bisect import insort


def matrix_sum(matrix, available_col, memo={tuple():0}):
    key = tuple(available_col)
    if key in memo:
        return memo[key]
    
    row = len(matrix) - len(available_col)
    
    max_sum = float('-inf')
    for col in available_col:
        available_col.remove(col)
        max_sum = max(max_sum, matrix[row][col] + matrix_sum(matrix, available_col, memo))
        insort(available_col, col)
    
    memo[key] = max_sum
    return max_sum


matrix = []
with open('input_files\\0345_matrix.txt', 'r') as f:
    for line in f:
        matrix.append([int(val) for val in line.strip().split()])

print(matrix_sum(matrix, list(range(len(matrix)))))
