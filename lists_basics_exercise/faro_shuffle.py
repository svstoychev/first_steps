# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved,
# such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once,
# gives ['ace', 'four', 'two', 'five', 'three', 'six']
#
# Write a program that receives a single string (cards separated by space)
# and on the second line receives a count of faro shuffles that should be made.
# Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

deck_of_cards = input().split()
shuffles_count = int(input())
lenght_two_sides = int((len(deck_of_cards) // 2))
for i in range(len(deck_of_cards)):
    left_side = deck_of_cards[:lenght_two_sides]
    right_side = deck_of_cards[lenght_two_sides:]
    new_deck = []
    for j in range (len(left_side)):
        new_deck.append(left_side[j])
        new_deck.append(right_side[j])
    deck_of_cards = new_deck
print(new_deck)
