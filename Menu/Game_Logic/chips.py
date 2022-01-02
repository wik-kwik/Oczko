class Chips:  # zetony/coinsy
    def __init__(self):
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):          # potem trzeba dodac 2 kolejne dla wygranej/przegranej
        self.total -= self.bet   # przez doubla
