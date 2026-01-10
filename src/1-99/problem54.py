from collections import Counter

CARDS = '23456789TJQKA'
CARD_VALUES = {card: val for val, card in enumerate(CARDS)}
STRAIGHTS = [(v, v-1, v-2, v-3, v-4) for v in range(len(CARDS) - 1, 3, -1)]
RANKS = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (), (), (3, 2), (4, 1)]

def get_hand_score(hand):
    counts = Counter(card[0] for card in hand)
    sorted_counts = sorted(((card_count, CARD_VALUES[card]) for card, card_count in counts.items()), reverse=True)
    score = list(zip(*sorted_counts))

    if score[0] in RANKS: # Figure
        score[0] = RANKS.index(score[0])
    else: # High card
        score[0] = 0
    if len(set(card[1] for card in hand)) == 1: # Flush
        score[0] = 5
    if score[1] in STRAIGHTS:
        score[0] = 8 if score[0] == 5 else 4  # 8: Straight Flush, 4: Straight
    return score

nb_win_p1 = 0
with open('input_files\\0054_poker.txt', 'r') as f:
    for line in f:
        hand = line.split()
        player1, player2 = hand[:5], hand[5:]
        if get_hand_score(player1) > get_hand_score(player2):
            nb_win_p1 += 1
print(nb_win_p1)