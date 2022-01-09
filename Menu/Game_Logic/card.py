class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.path = "image: url(:./images/Ikony kart/1/" + self.rank.lower() + "_of_" + self.suit.lower() + ".png);/"

    def __str__(self):
        return self.rank + ' of ' + self.suit
