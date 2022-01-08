from Game_Logic.replay import Replay
from Game_Logic.deck import Deck
import Game_Logic.blackjack as blackjack
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql
from timer import Timer


class FrontendLogic:
    def __init__(self, board):
        self.board = board
        self.number_of_players = board.playersNumber + board.computersNumber
        self.players = board.players
        db = sql.connect('database.db')  # łączymy się do bazy
        c = db.cursor()  # dodajemy kursor
        query = "SELECT decks from settings"
        c.execute(query)
        db.commit()
        result = c.fetchone()
        self.number_of_decks = result[0]
        self.replay = Replay()
        self.decision = 'wait'

    def clicked_hit(self):
        self.decision = 'hit'

    def clicked_stand(self):
        self.decision = 'stand'

    def check_if_clicked(self):
        print(self.timer.current_time)

    def start_game(self):
        deck = Deck()
        deck.deck = deck.deck * self.number_of_decks
        deck.shuffle_cards()
        self.replay.add_players(self.players)

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

                        # print("Playing: " + player.name + " value: " + str(player.hand.value))
                        # if player.playing is True:
                        #     decision = blackjack.hit_or_stand(deck, player)
                        #     self.replay.add_move(decision, player.player_number, player.hand.new_card)
                        #     print("value: " + str(player.hand.value))
                        #     if len(deck.deck) == 0:
                        #         playing = False
                        #         playing_round = False
                        #         break

                    # playing_round = blackjack.check_if_round_over(self.players)

            #     self.replay.add_round_to_game_replay()
            #     blackjack.add_points(self.players)

            # else:
            #     break
