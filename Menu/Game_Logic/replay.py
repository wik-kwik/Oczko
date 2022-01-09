from .convert_methods import Convert
from .card import Card


class Replay:  # powtorki
    def __init__(self):
        self.round_replay = []
        self.replay = []
        self.convert = Convert()

    def add_players(self, players):
        players_strings = []
        for player in players:
            players_strings.append(player.name + str(player.player_number))

        self.replay.append(players_strings)

    def add_first_hands(self, players):  # zapis pierwszej reki
        first_hand = ""
        for player in players:
            for card in player.hand.cards:
                first_hand += self.convert.convert_card_to_string(card)

        self.round_replay = [first_hand]

    def add_move(self, decision, player_number, card):
        move = str(player_number)
        if decision is True:
            move += "H"
            move += self.convert.convert_card_to_string(card)
            self.round_replay.append(move)

        else:
            move += "S"
            self.round_replay.append(move)

        # print(self.replay)

    def add_round_to_game_replay(self):
        self.replay.append(self.round_replay)
