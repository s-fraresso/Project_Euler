def square_sum(n):
    return (n * (n + 1) // 2)**2

def sum_of_squares(n):
    return n * (n + 1) * (2*n + 1) // 6

def sum_square_difference(n):
    return square_sum(n) - sum_of_squares(n)


print(sum_square_difference(100))