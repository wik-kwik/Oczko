from Game_Logic.replay import Replay
from Game_Logic.deck import Deck
import Game_Logic.blackjack as blackjack
import sqlite3 as sql


class FrontendLogic:
    def __init__(self, board, players):
        self.board = board
        self.number_of_players = board.playersNumber + board.computersNumber
        self.players = players
        db = sql.connect('database.db')  # łączymy się do bazy
        c = db.cursor()  # dodajemy kursor
        query = "SELECT number_of_decks from settings"
        c.execute(query)
        db.commit()
        result = c.fetchone()
        self.number_of_decks = result[0]

    def clicked_hit(self):
        print("hit")

    def clicked_stand(self):
        print("es")

    def start_game(self):
        deck = Deck()
        deck.deck = deck.deck * self.number_of_decks
        deck.shuffle_cards()
        replay = Replay()
        replay.add_players(self.players)
        playing = True

        # while len(deck.deck) > self.number_of_players * 2:
        #     if playing:
        #         playing_round = True

        #         for player in self.players:
        #             player.start_round(deck)

        #         replay.add_first_hands(self.players)

        #         while playing_round:  # round loop
        #             for player in self.players:
        #                 print("Playing: " + player.name + " value: " + str(player.hand.value))
        #                 if player.playing is True:
        #                     decision = blackjack.hit_or_stand(deck, player)
        #                     replay.add_move(decision, player.player_number, player.hand.new_card)
        #                     print("value: " + str(player.hand.value))
        #                     if len(deck.deck) == 0:
        #                         playing = False
        #                         playing_round = False
        #                         break

        #             playing_round = blackjack.check_if_round_over(self.players)

        #         replay.add_round_to_game_replay()
        #         blackjack.add_points(self.players)

        #     else:
        #         break
