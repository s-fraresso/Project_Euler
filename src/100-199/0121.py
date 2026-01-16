from fractions import Fraction
from itertools import combinations
from math import factorial


def probability_of_winning(nb_turns):
    all_blue_prob = Fraction(1, factorial(nb_turns + 1))
    prob_total = Fraction(0)
    for nb_red in range(nb_turns // 2 if nb_turns % 2 == 0 else nb_turns // 2 + 1):
        for red_turns in combinations(range(nb_turns), nb_red):
            prob = all_blue_prob
            for turn in red_turns:
                prob *= (turn + 1)
            prob_total += prob
    return prob_total.denominator // prob_total.numerator


print(probability_of_winning(15))
