import random
from .card import Card
from .cards import Cards

cards = Cards()
suits = cards.suits
ranks = cards.ranks


class Deck:  # talia kart ugulem
    def __init__(self):
        self.deck = []  # lista, ktora wypelnimy kartami i otrzymamy talie kart
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle_cards(self):  # wiadomo co, wiadomo kogo
        random.shuffle(self.deck)

    def deal(self):  # wybieranie karty z talii
        single_card = self.deck.pop()
        return single_card
