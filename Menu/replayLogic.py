from Game_Logic.deck import Deck
from Game_Logic.hand import Hand
from Game_Logic.convert_methods import Convert
import Game_Logic.blackjack as blackjack
import sqlite3 as sql

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

        j = 1
        while j < len(self.replay[1]):
            player = self.players[int(self.replay[1][j][0]) - 1]
            if self.replay[1][j][1] == "H":
                card = self.replay[1][j][-2:]
                blackjack.hit_on_replays(self.convert.convert_string_to_card(card), self.players[int(self.replay[1][j][0]) - 1].hand)

            if self.replay[1][j][1] == "S":
                pass

            j += 1

    # def player_change(self):
    #     self.reset_card_png()
    #     while True:
    #         if self.current_player_index + 1 < self.number_of_players:
    #             self.current_player_index += 1

    #         else:
    #             self.current_player_index = 0

    #         if self.players[self.current_player_index].playing is True:
    #             break

    #         else:
    #             continue

    #     self.current_player = self.players[self.current_player_index]
    #     self.board.change_player()
    #     self.set_player_labels()
    #     # print(self.current_player)

    def clicked_hit(self):
        decision = 'hit'
        decision_bool = blackjack.hit_or_stand(self.deck, self.current_player, decision)
        if self.current_player.hand.value >= 21:
            self.current_player.playing = False

        elif self.check_if_round_over() is True:
            self.board.round_over()

        else:
            self.player_change()

    def clicked_stand(self):
        decision = 'stand'
        decision_bool = blackjack.hit_or_stand(self.deck, self.current_player, decision)

    def decision_ai(self):
        decision_bool = blackjack.hit_or_stand(self.deck, self.current_player, "")

    def set_player_labels(self):
        for i in range(len(self.current_player.hand.cards)):
            aux_path = "image: url(:/images/" + self.current_player.hand.cards[i].rank.lower() + "_of_" + self.current_player.hand.cards[i].suit.lower() + ".png);"
            self.board.boardLabels.labels[self.current_player_index][i].setStyleSheet(aux_path)
            # print(aux_path)
            # self.board.boardLabels.labels[self.current_player_index][i].setStyleSheet("image: url(:/images/ace_of_clubs.png);")

    def reset_card_png(self):
        for i in range(len(self.players)):
            for j in range(len(self.board.boardLabels.labels[i])):
                self.board.boardLabels.labels[i][j].setStyleSheet("")

        for i in range(len(self.players)):
            for j in range(len(self.players[i].hand.cards)):
                self.board.boardLabels.labels[i][j].setStyleSheet(self.board.path)

    def show_cards_on_replay(self):
        for i in range(len(self.players)):
            for j in range(len(self.boardLabels.labels[i].hand.cards)):
                aux_path = "image: url(:/images/" + self.current_player.hand.cards[i].rank.lower() + "_of_" + self.current_player.hand.cards[i].suit.lower() + ".png);"
                self.board.boardLabels.labels[self.current_player_index][i].setStyleSheet(aux_path)

    # def check_if_round_over(self):
    #     active_players = 0
    #     for player in self.players:
    #         if player.playing is True:
    #             active_players += 1

    #     if active_players < 2:
    #         self.winners = blackjack.add_points(self.players)

    #         return True
    #     else:
    #         return False
