import random
from sprite import CardSprite

class Card():
    def __init__(self, card_values):
        self.values = card_values
        # creates a random id number for each card.
        # this is important to keep track of cards that are otherwise identical.
        self.values['id'] = random.randint(0, 999999)

        # can be hand, placed, pot, deck, etc..
        self.state = None
