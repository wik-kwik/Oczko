import random
from .player import Player
from .hand import Hand
# from card import Card
from .cards import Cards
# from deck import Deck
# from replay import Replay
from .convert_methods import Convert
import sqlite3 as sql

cards = Cards()
suits = cards.suits
ranks = cards.ranks
values = cards.values
playing = True  # sprawdzanie, czy pilka nadal w grze


def take_bet(chips):  # wez coinsy od gracza
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?: "))
        except ValueError:
            print("Please type in a number: ")
        else:
            if chips.bet > chips.total:
                print("Your bet can't exceed 1000!")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())


def hit_on_replays(card, hand):
    hand.add_card(card)


def hit_or_stand(deck, player, decision):  # zapytaj gracza, czy chce podbijac dalej
    if player.type == "player":
        if decision == 'hit':
            hit(deck, player.hand)
            # update_card_stat(player.hand.new_card)
            player.cards_played += 1
            update_cards(player.name)
            return True

        elif decision == 'stand':
            update_cards(player.name)
            update_cards(player.name)
            player.playing = False
            return False

    if player.type == "ceasy":  # easy (losowe decyzje)
        ask = bool(random.getrandbits(1))
        if ask is True and player.hand.value < 21:
            hit(deck, player.hand)
            # update_card_stat(player.hand.new_card)
            player.cards_played += 1
            return True

        else:
            player.playing = False
            return False

    if player.type == "cmedium":  # medium (bierze karte gdy value reki <= 17)
        if player.hand.value <= 17:
            hit(deck, player.hand)
            # update_card_stat(player.hand.new_card)
            player.cards_played += 1
            return True

        else:
            player.playing = False
            return False

    if player.type == "chard":  # hard (podglada jaka karta bedzie nastepna)
        if player.hand.value + values[deck.deck[len(deck.deck) - 1].rank] > 21:
            player.playing = False
            return False

        else:
            hit(deck, player.hand)
            # update_card_stat(player.hand.new_card)
            player.cards_played += 1
            return True


def check_if_round_over(players):  # sprawdzenie czy wszyscy gracze skonczyli runde
    playing_round = False

    for player in players:
        if player.playing is True:
            playing_round = True
            break

    return playing_round


def add_points(players):  # dodawanie punktow po rundzie
    players_max = []
    for player in players:
        if player.hand.value > 21 and player.check_if_pers() is False:  # sprawdzenie czy gracz nie spalil reki
            pass

        elif len(players_max) == 0 or player.hand.value == players_max[0].hand.value:
            players_max.append(player)

        elif player.hand.value > players_max[0].hand.value:
            players_max.clear()
            players_max = [player]

    return players_max


def update_cards(player):
    try:
        db = sql.connect('database.db')  # łączymy się do bazy
        c = db.cursor()  # dodajemy kursor


        query = "UPDATE users SET cards_used = cards_used + 1 where username = '{}'".format(player)
        c.execute(query)
        db.commit()

    except sql.Error as e:
        print("sth wrong with update")


