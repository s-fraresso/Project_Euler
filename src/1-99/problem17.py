letter_count_dict = {
    0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,
    10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8,
    20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 
    100:10, 200:10, 300:12, 400:11, 500:11, 600:10, 700:12, 800:12, 900:11,
}

def count_letters(number):
    if number <= 20:
        return letter_count_dict[number]
    elif number < 100:
        return letter_count_dict[(number // 10) * 10] + count_letters(number % 10)
    elif number < 1000:
        if number % 100 == 0:
            return letter_count_dict[(number // 100) * 100]
        else:
            return letter_count_dict[(number // 100) * 100] + count_letters(number % 100) + 3 # and
    else:
        return 11 # 1000


print(count_letters(342))
print(count_letters(115))
print(sum(count_letters(n) for n in range(1, 1000 + 1)))