from .cards import Cards

cards = Cards()
ranks = cards.ranks
values = cards.values


class Hand:  # odkrywanie kart
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # specjalnie miejsce dla ich, no bo specjalne są (maja wartosc albo 1 albo 11)
        self.new_card = any

    def add_card(self, card):  # dobieranie karty zawodnikom
        self.cards.append(card)
        self.new_card = card
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
