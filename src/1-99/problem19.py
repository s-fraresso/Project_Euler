year = 1901
month = 0 # january
day = 0 # 1st
week_day = 1 # tuesday


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_last_day_of_month(day, month, year):
    return (month in (3, 5, 8, 10) and day == 29) \
            or (month in (0, 2, 4, 6, 7, 9, 11) and day == 30) \
            or (month == 1 and ((is_leap_year(year) and day == 28) or (not is_leap_year(year) and day == 27)))


nb_special_sundays = 0

while year <= 2000:
    if week_day == 6 and day == 0:
        nb_special_sundays += 1
    week_day = (week_day + 1) % 7
    if is_last_day_of_month(day, month, year):
        day = 0
        month = (month + 1) % 12
        if month == 0:
            year += 1
    else:
        day += 1

print(nb_special_sundays)