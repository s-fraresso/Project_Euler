card_values = {"2":0, "3":1, "4":2, "5":3, "6":4, "7":5, "8":6, "9":7, "T":8, "J":9, "Q":10, "K":11, "A":12}

def sort_hand(hand):
    return sorted(hand, key=lambda card:card_values[card[0]])

def is_royal_flush(hand):
    return is_flush(hand) and hand[0][0] == "T" and hand[4][0] == "A"

def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)

def is_four_of_a_kind(hand):
    return hand[0][0] == hand[3][0] or hand[1][0] == hand[4][0]

def is_full_house(hand):
    return (hand[0][0] == hand[2][0] and hand[3][0] == hand[4][0]) or (hand[2][0] == hand[4][0] and hand[0][0] == hand[1][0])

def is_flush(hand):
    return all(hand[i][1] == hand[i + 1][1] for i in range(4))

def is_straight(hand):
    return all(card_values[hand[i][0]] == card_values[hand[i + 1][0]] + 1 for i in range(4))

def is_three_of_a_kind(hand):
    return hand[0][0] == hand[2][0] or hand[1][0] == hand[3][0] or hand[2][0] == hand[4][0]

def is_two_pairs(hand):
    return (hand[0][0] == hand[1][0] and (hand[2][0] == hand[3][0] or hand[3][0] == hand[4][0])) or (hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0])

def is_one_pair(hand):
    return any(hand[i][0] == hand[i + 1][0] for i in range(4))

def compute_hand_value(hand):
    total = 0
    is_special = True

    if is_royal_flush(hand):
        total += 417_000_000
    elif is_straight_flush(hand):
        total += 404_000_000
        total += 1_000_000 * card_values[hand[4][0]]
    elif is_four_of_a_kind(hand):
        total += 391_000_000
        total += 1_000_000 * card_values[hand[2][0]]
    elif is_full_house(hand):
        total += 222_000_000
        if hand[0][0] == hand[2][0]:
            total += 1_000_000 * card_values[hand[4][0]]
            total += 1_000_000 * 13 * card_values[hand[2][0]]
        else:
            total += 1_000_000 * card_values[hand[1][0]]
            total += 1_000_000 * 13 * card_values[hand[4][0]]
    elif is_flush(hand):
        total += 209_000_000
        total += 1_000_000 * card_values[hand[4][0]]
    elif is_straight(hand):
        total += 196_000_000
        total += 1_000_000 * card_values[hand[4][0]]
    elif is_three_of_a_kind(hand):
        total += 183_000_000
        total += 1_000_000 * card_values[hand[2][0]]
    elif is_two_pairs(hand):
        total += 14_000_000
        total += 1_000_000 * card_values[hand[1][0]]
        total += 1_000_000 * 13 * card_values[hand[3][0]]
    elif is_one_pair(hand):
        total += 1_000_000
        for i in range(len(hand) - 1):
            if hand[i][0] == hand[i + 1][0]:
                total += 1_000_000 * card_values[hand[i][0]]
                break
        is_special = False
    else:
        is_special = False

    for i in range(len(hand)):
        total += card_values[hand[i][0]] * 13**i

    return total, is_special


def count_P1_wins(input_file):
    wins = 0
    with open(input_file, 'r') as f:
        for line in f:
            line = line[:-1].split(' ')
            hand1, hand2 = sort_hand(line[:5]), sort_hand(line[5:])
            results = compute_hand_value(hand1), compute_hand_value(hand2)
            if results[0][0] > results[1][0]:
                wins += 1
            if results[0][1] and results[1][1]:
                print(hand1, hand2, results[0][0] > results[1][0])
    return wins

print(count_P1_wins("input_files\\0054_poker.txt"))