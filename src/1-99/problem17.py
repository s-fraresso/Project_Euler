number_letter_dict = {
1: 3,
2: 3,
3: 5,
4: 4,
5: 4,
6: 3,
7: 5,
8: 5,
9: 4,
10: 3,
11: 6,
12: 6,
13: 8,
14: 8,
15: 7,
16: 7,
17: 9,
18: 9,
19: 8,
20: 6,
30: 6,
40: 5,
50: 5,
60: 5,
70: 7,
80: 7,
90: 6,
}

def number_letter_count(n):
    if n == 0:
        return 0
    if n < 20:
        return number_letter_dict[n]
    if n < 100:
        return number_letter_dict[n // 10 * 10] + number_letter_count(n % 10)
    if n == 1000:
        return 11
    if n % 100 != 0:
        return number_letter_dict[n // 100] + 7 + 3 + number_letter_count(n % 100)
    else:
        return number_letter_dict[n // 100] + 7


def number_letter_up_to(n):
    nb_letter = 0
    for i in range(1, n + 1):
        nb_letter += number_letter_count(i)
    return nb_letter

print(number_letter_up_to(1000))