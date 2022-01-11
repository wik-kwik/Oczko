from Game_Logic.deck import Deck
from Game_Logic.hand import Hand
from Game_Logic.convert_methods import Convert
import Game_Logic.blackjack as blackjack
import sqlite3 as sql
import time

from Menu.Game_Logic.player import Player


class FrontendLogic:
    def __init__(self, replayBoard):
        self.board = replayBoard
        self.replay = replayBoard.replay
        self.players = replayBoard.players
        self.number_of_players = len(self.players)
        self.winners = []
        self.conver = Convert()

    def start_game(self):
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]
        self.reset_card_png()
        self.set_player_labels()

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

        j = 1
        while j < len(self.replay[1]):
            player = self.players[int(self.replay[1][j][0]) - 1]
            if self.replay[1][j][1] == "H":
                card = self.replay[1][j][-2:]
                blackjack.hit_on_replays(self.convert.convert_string_to_card(card), self.players[int(self.replay[1][j][0]) - 1].hand)
                self.show_cards_on_replay()

            if self.replay[1][j][1] == "S":
                pass

            j += 1

        self.winnners = blackjack.add_points(self.players)
        self.board.game_ends()

    def show_cards_on_replay(self):
        for i in range(len(self.players)):
            for j in range(len(self.boardLabels.labels[i].hand.cards)):
                aux_path = "image: url(:/images/" + self.current_player.hand.cards[i].rank.lower() + "_of_" + self.current_player.hand.cards[i].suit.lower() + ".png);"
                self.board.boardLabels.labels[self.current_player_index][i].setStyleSheet(aux_path)
