from .card import Card
from .cards import Cards

cards = Cards()
suits = cards.suits
ranks = cards.ranks
values = cards.values


class Convert:
    def convert_card_to_string(self, card):  # konwersja na string dla ulatwienia zapisu w db
        card_string = ""

        if card.suit == "Spades":
            card_string += "S"

        elif card.suit == "Diamonds":
            card_string += "D"

        elif card.suit == "Hearts":
            card_string += "H"

        elif card.suit == "Clubs":
            card_string += "C"

        if values[card.rank] <= 9:
            card_string += str(values[card.rank])

        elif card.rank == "Ten":
            card_string += "T"

        elif card.rank == "Jack":
            card_string += "J"

        elif card.rank == "Queen":
            card_string += "Q"

        elif card.rank == "King":
            card_string += "K"

        elif card.rank == "Ace":
            card_string += "A"

        return card_string

    def convert_string_to_card(self, card_string):
        if card_string[0] == "S":
            suit = "Spades"

        elif card_string[0] == "D":
            suit = "Diamonds"

        elif card_string[0] == "H":
            suit = "Hearts"

        elif card_string[0] == "C":
            suit = "Clubs"

        if card_string[1] == "2":
            rank = "Two"

        elif card_string[1] == "3":
            rank = "Three"

        elif card_string[1] == "4":
            rank = "Four"

        elif card_string[1] == "5":
            rank = "Five"

        elif card_string[1] == "6":
            rank = "Six"

        elif card_string[1] == "7":
            rank = "Seven"

        elif card_string[1] == "8":
            rank = "Eight"

        elif card_string[1] == "9":
            rank = "Nine"

        elif card_string[1] == "T":
            rank = "Ten"

        elif card_string[1] == "J":
            rank = "Jack"

        elif card_string[1] == "Q":
            rank = "Queen"

        elif card_string[1] == "K":
            rank = "King"

        elif card_string[1] == "A":
            rank = "Ace"

        return Card(suit, rank)
