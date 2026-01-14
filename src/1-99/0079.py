with open('input_files\\0079_keylog.txt', 'r') as f:
    attempts = [list(map(int, line.strip())) for line in f.readlines()]

digits = [0, 1, 2, 3, 6, 7, 8, 9]
passcode = ''
while digits:
    next_possible_digits = digits.copy()
    for a in attempts:
        for d in a[1:]:
            if d in next_possible_digits:
                next_possible_digits.remove(d)

    next_digit = next_possible_digits[0]
    digits.remove(next_digit)
    passcode += str(next_digit)
    for a in attempts:
        if next_digit in a:
            a.remove(next_digit)

print(passcode)