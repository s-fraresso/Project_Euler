from math import log

def largest_exponential(input_file):
    largest = float('-inf')
    best_line = 0
    l = 1
    with open(input_file, 'r') as f:
        for line in f:
            base, exponent = [int(val) for val in line.split(',')]
            log_val = exponent * log(base)
            if log_val > largest:
                largest = log_val
                best_line = l
            l += 1
    return best_line

print(largest_exponential("input_files\\0099_base_exp.txt")) # 709