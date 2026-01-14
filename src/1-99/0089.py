numeral_value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
threshold_letters = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
                    (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def count_saved_characters(input_file):
    numbers, nb_character_original = read_roman_numbers(input_file)
    return nb_character_original - sum(len(itorom(n)) for n in numbers)


def itorom(number):
    if number == 0:
        return ""
    
    for tl in threshold_letters:
        if number >= tl[0]:
            return tl[1] + itorom(number - tl[0])
        

def romtoi(roman):
    number = 0
    for i in range(len(roman)):
        if i < len(roman) - 1 and numeral_value[roman[i + 1]] > numeral_value[roman[i]]:
            number -= numeral_value[roman[i]]
        else:
            number += numeral_value[roman[i]]
    return number


def read_roman_numbers(input_file):
    numbers = []
    nb_character = 0
    with open(input_file, 'r') as f:
        for line in f:
            numbers.append(romtoi(line.strip()))
            nb_character += len(line.strip())
    return numbers, nb_character


print(count_saved_characters("input_files\\0089_roman.txt"))