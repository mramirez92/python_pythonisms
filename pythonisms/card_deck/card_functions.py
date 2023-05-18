from card_deck import Deck
from random import choice


deck = Deck()

# print(len(deck))
# print(deck[:3])
# print(choice(deck))

"""__getitem__ allows us to iterate over cards"""
# for card in deck:
#     print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)

