from Game_Logic.replay import Replay
from Game_Logic.deck import Deck
import Game_Logic.blackjack as blackjack
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql


class FrontendLogic:
    def __init__(self, board):
        self.board = board
        self.number_of_players = board.playersNumber + board.computersNumber
        self.players = board.players

    def start_game(self):
        db = sql.connect('database.db')  # łączymy się do bazy
        c = db.cursor()  # dodajemy kursor
        query = "SELECT decks from settings"
        c.execute(query)
        db.commit()
        result = c.fetchone()
        self.number_of_decks = result[0]
        self.replay = Replay()
        self.deck = Deck()
        self.deck.deck = self.deck.deck * self.number_of_decks
        self.deck.shuffle_cards()
        self.replay.add_players(self.players)
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]
        self.set_player_labels()

    def player_change(self):
        if self.current_player_index + 1 < self.number_of_players:
            self.current_player_index += 1

        else:
            self.current_player_index = 0

        self.current_player = self.players[self.current_player_index]
        print(self.current_player)

    def clicked_hit(self):
        decision = 'hit'
        blackjack.hit_or_stand(self.deck, self.current_player, decision)
        self.player_change()

    def clicked_stand(self):
        decision = 'stand'
        blackjack.hit_or_stand(self.deck, self.current_player, decision)
        self.player_change()

    def set_player_labels(self):
        for i in range(len(self.current_player.cards)):
            self.board.boardLabels.labels[self.current_player_index][i].setText(self.current_player.hand.hand).setText(self.current_player.cards[i].path)


    # def start_game(self):

        # while self.current_time >= 0:
        #     # timer = QtCore.QTimer()  # set up your QTimer
        #     # timer.timeout.connect(self.check_if_clicked())  # connect it to your update function
        #     # timer.start(1000)  # set it to timeout in 5000 ms
        #     time.sleep(1)
        #     self.current_time = self.current_time - 1


        # while len(deck.deck) > self.number_of_players * 2:
        #     if playing:
        #         playing_round = True

        #         for player in self.players:
        #             player.start_round(deck)

        #         self.replay.add_first_hands(self.players)

        #         while playing_round:  # round loop
        #             for player in self.players:
        #                 self.current_time = self.time
        #                 for self.current_time in range(self.time, 0):

        #                     time.sleep(1)

        #                 print("Playing: " + player.name + " value: " + str(player.hand.value))
        #                 if player.playing is True:
        #                     decision = blackjack.hit_or_stand(deck, player)
        #                     self.replay.add_move(decision, player.player_number, player.hand.new_card)
        #                     print("value: " + str(player.hand.value))
        #                     if len(deck.deck) == 0:
        #                         playing = False
        #                         playing_round = False
        #                         break

        #             playing_round = blackjack.check_if_round_over(self.players)

        #         self.replay.add_round_to_game_replay()
        #         blackjack.add_points(self.players)

        #     else:
        #         break
