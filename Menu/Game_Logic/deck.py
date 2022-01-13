import random
from .card import Card
from .cards import Cards
import sqlite3 as sql


class Deck:
    def __init__(self):
        self.deck = []  # lista, ktora wypelnimy kartami i otrzymamy talie kart
        self.cards = Cards()
        for suit in self.cards.suits:
            for rank in self.cards.ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle_cards(self):
        random.shuffle(self.deck)

    def deal(self):  # wybieranie karty z talii
        single_card = self.deck.pop()
        self.update_card_stat(single_card)
        return single_card

    def update_card_stat(self, name):
        try:
            db = sql.connect('database.db')  # łączymy się do bazy
            c = db.cursor()  # dodajemy kursor

            query = "UPDATE cards SET sum = sum + 1 where name = '{}'".format(name)
            c.execute(query)
            db.commit()

        except sql.Error as e:
            print("sth wrong with update")
