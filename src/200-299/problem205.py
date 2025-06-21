def ways_to_roll(total, nb_faces, nb_dice, memo = {}):
    if (total, nb_faces, nb_dice) not in memo:
        if total < nb_dice or nb_dice == 0 or total > nb_dice * nb_faces:
            memo[(total, nb_faces, nb_dice)] = 0
        elif nb_dice == 1:
            memo[(total, nb_faces, nb_dice)] = 1
        else:
            nb_ways = 0
            for k in range(1, nb_faces + 1):
                nb_ways += ways_to_roll(total - k, nb_faces, nb_dice - 1, memo)
            memo[(total, nb_faces, nb_dice)] = nb_ways
    return memo[(total, nb_faces, nb_dice)]


def odds_of_P1_winning(nb_dice1, nb_faces1, nb_dice2, nb_faces2):
    roll_odds1 = {roll: ways_to_roll(roll, nb_faces1, nb_dice1) for roll in range(nb_dice1, nb_dice1 * nb_faces1 + 1)}
    roll_odds2 = {roll: ways_to_roll(roll, nb_faces2, nb_dice2) for roll in range(nb_dice2, nb_dice2 * nb_faces2 + 1)}    
    return sum(sum(roll_odds2[roll2] for roll2 in filter(lambda r: r < roll1, roll_odds2.keys())) * roll_odds1[roll1] for roll1 in roll_odds1) / (nb_faces1**nb_dice1 * nb_faces2**nb_dice2)


print(odds_of_P1_winning(9, 4, 6, 6)) # 0.5731440767829801 ~= 0.5731441