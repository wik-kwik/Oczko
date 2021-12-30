import random

suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}

playing = True  # sprawdzanie, czy pilka nadal w grze


class Player:
    def __init__(self, name, type, player_number):
        self.name = name
        self.type = type
        self.player_number = player_number
        self.points = 0
        self.playing = True  # sprawdzenie czy gracz uczestniczy w rundzie
        self.cards_played = 0

    def start_round(self, deck):  # dobranie reki na start rundy
        self.hand = Hand()
        self.hand.add_card(deck.deal())
        self.hand.add_card(deck.deal())
        self.cards_played += 2
        self.playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


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

    def adjust_for_ace(self):  # 1 lub 11 dla asa
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:  # zetony/coinsy
    def __init__(self):
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):          # potem trzeba dodac 2 kolejne dla wygranej/przegranej
        self.total -= self.bet   # przez doubla

class Replay:  # powtorki
    def __init__(self):
        self.round_replay = []
        self.replay = []

    def add_players(self, players):
        players_strings = []
        for player in players:
            players_strings.append(player.name + str(player.player_number))
        
        self.replay.append(players_strings)
 
    def add_first_hands(self, players):  # zapis pierwszej reki
        first_hand = ""
        for player in players:
            for card in player.hand.cards:
                first_hand += convert_card_to_string(card)

        self.round_replay.append(first_hand)
        print(self.round_replay)

    def add_move(self, decision, player_number, card, round_number):
        move = str(round_number)
        move += str(player_number)
        if decision is True:
            move += "H"
            move += convert_card_to_string(card)
            self.round_replay.append(move)
            print(self.round_replay)

        else:
            move += "S"

    def add_round_to_game_replay(self):
        self.replay.append(self.round_replay)
        print(self.replay)


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

def convert_card_to_string(card):  # konwersja na string dla ulatwienia zapisu w db
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

def convert_string_to_card(card_string):
    if card_string[0] == "S":
        suit = "Spades"
    
    elif card_string[0] == "D":
        suit = "Diamonds"

    elif card_string[0]== "H":
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

while len(deck.deck) > number_of_players * 2:
    if playing:
        print("Welcome to Blackjack!")
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