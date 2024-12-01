from sys import stdin

scratch_cards_points = 0 
for line in stdin:
    card_split = line.split(":")
    numbers = card_split[1].split("|")
    picked_numbers = numbers[0].split()
    winning_numbers = numbers[1].split()

    count_winning_numbers = 0
    for picked_num in picked_numbers:
        if picked_num in winning_numbers:
            count_winning_numbers += 1
    if count_winning_numbers != 0:
        scratch_cards_points += pow(2,count_winning_numbers - 1)

print(scratch_cards_points)