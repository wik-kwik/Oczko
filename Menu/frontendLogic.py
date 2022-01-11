from Game_Logic.replay import Replay
from Game_Logic.deck import Deck
import Game_Logic.blackjack as blackjack
import sqlite3 as sql
from PyQt5 import QtWidgets
import bustPopout


class FrontendLogic:
    def __init__(self, board):
        self.board = board
        self.number_of_players = board.playersNumber + board.computersNumber
        self.players = board.players
        self.winners = []

    def start_game(self):
        db = sql.connect('database.db')  # łączymy się do bazy
        c = db.cursor()  # dodajemy kursor
        query = "SELECT decks from settings"
        c.execute(query)
        db.commit()
        result = c.fetchone()
        self.number_of_decks = result[0]
        if self.number_of_decks == 0:
            self.number_of_decks = 1
        self.replay = Replay()
        self.deck = Deck()
        self.deck.deck = self.deck.deck * self.number_of_decks
        self.deck.shuffle_cards()
        self.replay.add_players(self.players)
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]
        for player in self.players:
            player.start_round(self.deck)

        self.reset_card_png()
        self.set_player_labels()
        self.check_if_round_over

    def player_change(self, decision):
        while True:
            if self.current_player_index + 1 < self.number_of_players:
                self.current_player_index += 1

            else:
                self.current_player_index = 0

            if self.players[self.current_player_index].playing is True:
                break

            else:
                continue

        self.current_player = self.players[self.current_player_index]
        self.board.change_player(decision)
        # print(self.current_player)

    def clicked_hit(self):
        decision = 'hit'
        decision_bool = blackjack.hit_or_stand(self.deck, self.current_player, decision)
        self.replay.add_move(decision_bool, self.current_player.player_number, self.current_player.hand.new_card)

        if self.current_player.hand.value >= 21:
            self.current_player.playing = False

        if self.current_player.hand.value > 21 and self.check_if_round_over() is False:
            self.window = QtWidgets.QMainWindow()
            self.ui = bustPopout.bustForm(self.board, self.current_player.name)
            self.ui.setupUi(self.window)
            self.window.show()

        if self.check_if_round_over() is True:
            self.board.round_over()

        else:
            self.set_player_labels()
            self.board.show_user_points()
            self.player_change(decision)

    def clicked_stand(self):
        decision = 'stand'
        decision_bool = blackjack.hit_or_stand(self.deck, self.current_player, decision)
        self.replay.add_move(decision_bool, self.current_player.player_number, self.current_player.hand.new_card)

        if self.check_if_round_over() is True:
            self.board.round_over()

        else:
            self.player_change(decision)

    def decision_ai(self):
        decision_bool = blackjack.hit_or_stand(self.deck, self.current_player, "")
        self.replay.add_move(decision_bool, self.current_player.player_number, self.current_player.hand.new_card)

        if decision_bool is True:
            if self.current_player.hand.value >= 21:
                self.current_player.playing = False

            if self.current_player.hand.value > 21 and self.check_if_round_over() is False:
                self.window = QtWidgets.QMainWindow()
                self.ui = bustPopout.bustForm(self.board, self.current_player.name)
                self.ui.setupUi(self.window)
                self.window.show()

        if self.check_if_round_over() is True:
            self.board.round_over()

        else:
            self.player_change("")

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

    def check_if_round_over(self):
        active_players = 0
        for player in self.players:
            if player.playing is True:
                active_players += 1

        if active_players == 0:
            self.winners = blackjack.add_points(self.players)
            self.replay.add_round_to_game_replay()

            return True
        else:
            return False
