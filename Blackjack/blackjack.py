import random
from player import Player
from hand import Hand
from card import Card
from cards import Cards
from deck import Deck
from replay import Replay

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
    hand.adjust_for_ace()


def hit_or_stand(deck, player):  # zapytaj gracza, czy chce podbijac dalej
    global playing

    while True:
        if player.type == "player":
            ask = input("Would you like to hit or stand? Please enter 'h' or 's': ")

            if ask[0].lower() == 'h':
                hit(deck, player.hand)
                player.cards_played += 1
                return True
            elif ask[0].lower() == 's':
                print("Player stands.")
                player.playing = False
                return False
            else:
                print("Sorry, I didn't understand that, please try again!")
                continue
            break

        if player.type == "ceasy":  # easy (losowe decyzje)
            ask = bool(random.getrandbits(1))
            if ask is True:
                print(player.name + " hits.")
                hit(deck, player.hand)
                player.cards_played += 1
                return True

            else:
                print(player.name + " stands.")
                player.playing = False
                return False

            break

        if player.type == "cmedium":  # medium (bierze karte gdy value reki <= 17)
            if player.hand.value <= 17:
                print(player.name + " hits.")
                hit(deck, player.hand)
                player.cards_played += 1
                return True

            else:
                print(player.name + " stands.")
                player.playing = False
                return False

            break

        if player.type == "chard":  # hard (podglada jaka karta bedzie nastepna)
            if player.hand.value + values[deck.deck[len(deck.deck) - 1].rank] > 21:
                if deck.deck[len(deck.deck) - 1].rank == 'Ace':
                    if player.hand.value + 1 <= 21:
                        print(player.name + " hits.")
                        hit(deck, player.hand)
                        player.cards_played += 1
                        return True

                    else:
                        print(player.name + " stands.")
                        player.playing = False
                        return False

                else:
                    print(player.name + " stands.")
                    player.playing = False
                    return False

            else:
                print(player.name + " hits.")
                hit(deck, player.hand)
                player.cards_played += 1
                return False

            break


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
        if player.hand.value > 21:  # sprawdzenie czy gracz nie spalil reki
            pass

        elif len(players_max) == 0 or player.hand.value == players_max[0].hand.value:
            players_max.append(player)

        elif player.hand.value > players_max[0].hand.value:
            players_max.clear()
            players_max = [player]

    for player in players_max:
        print(player.name + " " + str(player.hand.value))
        player.points += 1


deck = Deck()  # stworzenie talii
deck.shuffle_cards()

number_of_players = 4

player1 = Player("siema1", "player", 1)     # gracz
player2 = Player("siema2", "ceasy", 2)      # komputer latwy
player3 = Player("siema3", "cmedium", 3)    # komputer sredni
player4 = Player("siema4", "chard", 4)      # komputer trudny

players = [player1, player2, player3, player4]

replay = Replay()
replay.add_players(players)
print("Welcome to Blackjack!")


while len(deck.deck) > number_of_players * 2:
    if playing:
        playing_round = True

        player1.start_round(deck)
        player2.start_round(deck)
        player3.start_round(deck)
        player4.start_round(deck)

        round_number = 1

        replay.add_first_hands(players)

        while playing_round:  # round loop
            for player in players:
                print("Playing: " + player.name + " value: " + str(player.hand.value))
                if player.playing is True:
                    decision = hit_or_stand(deck, player)
                    replay.add_move(decision, player.player_number, player.hand.new_card, round_number)
                    print("value: " + str(player.hand.value))
                    if len(deck.deck) == 0:
                        playing = False
                        playing_round = False
                        break

            playing_round = check_if_round_over(players)

        round_number += 1
        replay.add_round_to_game_replay()
        add_points(players)

    else:
        break

# odczytywanie zapisu z replaya

i = 0
while i < len(replay):
    if i == 0:
        for player in replay[0]:
            pass

    i += 1
