def count_triangle_words(input_file):
    triangle_numbers = [1]
    for i in range(2, 50):
        triangle_numbers.append(triangle_numbers[i - 2] + i)

    nb_triangle_words = 0
    with open(input_file, 'r') as f:
        for line in f:
            for word in line.split(','):
                word = word[1:-1]
                if sum(ord(letter) - 64 for letter in word) in triangle_numbers:
                    nb_triangle_words += 1
    
    return nb_triangle_words

print(count_triangle_words("input_files\\0042_words.txt")) # 162
