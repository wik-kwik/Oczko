class Cards:
    def __init__(self):
        self.suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
        self.ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                      'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
        self.values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
                       'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
                       'Jack': 2, 'Queen': 3, 'King': 4, 'Ace': 11}
