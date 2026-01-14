import os

def name_value(name):
    value = 0
    for c in name:
        value += ord(c) - ord('A') + 1
    return value



def names_scores(input_file):
    total = 0
    names = []
    with open(input_file, 'r') as f:
        for line in f:
            names.extend([name.removeprefix("\"").removesuffix("\"") for name in line.split(',')])
    names.sort()
    for i in range(len(names)):
        total += (i + 1) * name_value(names[i])
    return total


print(names_scores("input_files\\0022_names.txt")) # 871198282