deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    shuffled_form = []
    mid_of_the_deck = len(deck_of_cards) // 2
    left_side = deck_of_cards[0: mid_of_the_deck]
    right_side = deck_of_cards[mid_of_the_deck::]

    for card_index in range(len(left_side)):
        shuffled_form.append(left_side[card_index])
        shuffled_form.append(right_side[card_index])

    deck_of_cards = shuffled_form

print(deck_of_cards)