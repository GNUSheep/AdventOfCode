from sys import stdin

scratch_cards_points = 0 

scratch_cards = []
which_card_current = 1
for line in stdin:
    scratch_cards.append(which_card_current)

    card_split = line.split(":")
    numbers = card_split[1].split("|")
    picked_numbers = numbers[0].split()
    winning_numbers = numbers[1].split()

    count_winning_numbers = 0
    for picked_num in picked_numbers:
        if picked_num in winning_numbers:
            count_winning_numbers += 1

    for _ in range(0, scratch_cards.count(which_card_current)):
        for x in range(which_card_current+1, count_winning_numbers+which_card_current+1):
            scratch_cards.append(x)

    which_card_current += 1
    
print(len(scratch_cards))