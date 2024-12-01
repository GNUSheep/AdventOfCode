from sys import stdin
from functools import cmp_to_key

cards = []
bids = {}
for line in stdin:
    cards.append(line.split()[0])
    bids[line.split()[0]] = line.split()[1]

def get_hand_type(card):
    x = list(card)
    count_cards = {i:x.count(i) for i in x}

    j_count = 0
    if "J" in count_cards:
        j_count = count_cards["J"]
        count_cards["J"] = 0

    hand_type_key = max(count_cards, key=count_cards.get)
    hand_type = count_cards[hand_type_key] + j_count
        
    if hand_type == 5:
        return 7
    if hand_type == 4:
        return 6
    if hand_type == 3:
        for card, count in count_cards.items():
            if count == 2 and card != hand_type_key:
                return 5
        return 4
    if hand_type == 2:
        for card, count in count_cards.items():
            if count == 2 and card != hand_type_key:
                return 3
        return 2
    if hand_type == 1:
        return 1

def card_value(x):
    if x == "A":
        return 14
    if x == "K":
        return 13
    if x == "Q":
        return 12
    if x == "J":
        return 1
    if x == "T":
        return 10
    return int(x)

def orderer(x, y):
    x_type = get_hand_type(x)
    y_type = get_hand_type(y)

    if x_type == y_type:
        for i in range(0, 5):
            if card_value(x[i]) > card_value(y[i]):
                return 1
            if card_value(x[i]) < card_value(y[i]):
                return -1 

    if x_type > y_type:
        return 1
    return -1

cards = sorted(cards, key=cmp_to_key(orderer))

total_winnings = 0
for i in range(0, len(cards)):
    total_winnings += int(bids[cards[i]]) * (i+1)
print(total_winnings)
