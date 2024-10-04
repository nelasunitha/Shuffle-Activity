import random
CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards without using random.shuffle()
# Using randint() is ok
def shuffle_deck(deck_of_cards):

    l = len(deck_of_cards)
    # iterating from the last index
    for i in range(l-1, 0, -1):
        j = random.randint(0, i)

        # swapping the cards starting from last index to random index
        deck_of_cards[i], deck_of_cards[j] = deck_of_cards[j], deck_of_cards[i]
    return deck_of_cards

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

shuffle_deck = shuffle_deck(deck_of_cards)
print(f"After shuffling: {shuffle_deck}")