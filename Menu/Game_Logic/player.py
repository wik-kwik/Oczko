from .hand import Hand


class Player:
    def __init__(self, name, type, player_number, labels):
        self.name = name
        self.type = type
        self.player_number = player_number
        self.labels = labels
        self.playing = True  # sprawdzenie czy gracz uczestniczy w rundzie
        self.cards_played = 0

    def start_round(self, deck):  # dobranie reki na start rundy
        self.hand = Hand()
        self.hand.add_card(deck.deal())
        self.hand.add_card(deck.deal())
        self.cards_played += 2
        self.playing = True
