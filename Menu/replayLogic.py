from Game_Logic.deck import Deck
from Game_Logic.hand import Hand
from Game_Logic.convert_methods import Convert
import Game_Logic.blackjack as blackjack
import sqlite3 as sql
from PyQt5 import QtCore
from Game_Logic.player import Player


class ReplayLogic:
    def __init__(self, replayBoard):
        self.board = replayBoard
        self.replay = replayBoard.replay
        self.players = replayBoard.players
        self.boardLabels = replayBoard.boardLabels
        self.number_of_players = len(self.players)
        self.winners = []
        self.convert = Convert()

    def start_game(self):
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]

        aux = self.number_of_players - 1
        first_hands = self.replay[1][0]
        while first_hands != "":
            first_hands, card = first_hands[:-2], first_hands[-2:]
            self.players[aux].hand = Hand()
            blackjack.hit_on_replays(self.convert.convert_string_to_card(card), self.players[aux].hand)
            first_hands, card = first_hands[:-2], first_hands[-2:]
            blackjack.hit_on_replays(self.convert.convert_string_to_card(card), self.players[aux].hand)
            aux = aux - 1

        self.show_cards_on_replay()

        self.aux_for_check = 1
        QtCore.QTimer.singleShot(1000, self.make_a_move)

        self.winnners = blackjack.add_points(self.players)
        self.board.game_ends()

    def make_a_move(self):
        print(self.aux_for_check)
        if self.replay[1][self.aux_for_check][1] == "H":
            card = self.replay[1][self.aux_for_check][-2:]
            blackjack.hit_on_replays(self.convert.convert_string_to_card(card), self.players[int(self.replay[1][self.aux_for_check][0]) - 1].hand)
            self.show_cards_on_replay()
            self.go_to_next_move()

        if self.replay[1][self.aux_for_check][1] == "S":
            self.go_to_next_move()

    def go_to_next_move(self):
        if self.aux_for_check < len(self.replay[1]) - 1:
            self.aux_for_check += 1
            QtCore.QTimer.singleShot(1000, self.make_a_move)

    def show_cards_on_replay(self):
        for i in range(len(self.players)):
            for j in range(len(self.players[i].hand.cards)):
                aux_path = "image: url(:/images/" + self.players[i].hand.cards[j].rank.lower() + "_of_" + self.players[i].hand.cards[j].suit.lower() + ".png);"
                self.board.boardLabels.labels[i][j].setStyleSheet(aux_path)
