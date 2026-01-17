def count_prize_strings(nb_days, can_be_late=True, memo={}):
    if nb_days == 0:
        return 1

    if (nb_days, can_be_late) in memo:
        return memo[(nb_days, can_be_late)]

    nb_prize_strings = count_prize_strings(nb_days - 1, can_be_late, memo) # Attended
    if can_be_late:
        nb_prize_strings += count_prize_strings(nb_days - 1, False, memo) # Late
    for nb_days_absent in range(1, min(3, nb_days + 1)): # At least one absence
        if nb_days > nb_days_absent: # need to close the absence block with attended or late
            nb_prize_strings += count_prize_strings(nb_days - (nb_days_absent + 1), can_be_late, memo) # attended after the absence
            if can_be_late:
                nb_prize_strings += count_prize_strings(nb_days - (nb_days_absent + 1), False, memo) # late after the absence
        else: # absent till the end
            nb_prize_strings += 1
    memo[(nb_days, can_be_late)] = nb_prize_strings
    return nb_prize_strings


print(count_prize_strings(30))