import random

class deck:
    suits = [
        "Diamonds",
        "Clubs",
        "Hearts",
        "Spades"
    ]
    cardnames = [
        "Ace",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King"
    ]
    def __init__(self):
        self.cards = []

    def shuffle(self):
        self.cards = list(range(52))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    @staticmethod
    def pointValue(cardid: int):
        return min(cardid % 13 + 1, 10)

    @staticmethod
    def cardString(cardid: int):
        return deck.cardnames[cardid % 13] + " of " + deck.suits[cardid // 13]



