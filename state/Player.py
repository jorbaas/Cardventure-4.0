from .card_values import *
from .Card import Card


class Player():
    def __init__(self, name):
        self.name = name

        # self.deck = [H_1, H_1, H_1, H_1, H_1, H_2, H_2, H_2, H_2, H_2,
        #              B_1, B_1, B_1, B_1, B_1, B_2, B_2, B_2, B_2, B_2,
        #              S_1, S_1, S_1, S_1, S_1, S_2, S_2, S_2, S_2, S_2,
        #              D_1, D_1, D_1, D_1, D_1, D_2, D_2, D_2, D_2, D_2]

        self.deck = [H_1, H_2, H_3, H_4,H_1, H_2, H_3, H_4,
             B_1, B_2, B_3, B_4,
             S_1, S_2, S_3, S_3, S_3, S_3,
             D_1, D_2, D_3,
             B_1, B_2, B_3, B_4,
             S_1, S_2,
             D_1, D_2, D_3, H_1, H_2, H_3, H_4,
             B_1, B_2, B_3, B_4,
             S_1, S_2,
             D_1, D_2, D_3, H_1, H_2, H_3, H_4,
             B_1, B_2, B_3, B_4,
             S_1, S_2,
             D_1, D_2, D_3
             ]
        # replaces all the dicts for card objects with random id
        for card_values in self.deck:
            card = card_values.copy()
            card = Card(card)
            card.state = 'deck'
            self.deck.remove(card_values)
            self.deck.insert(0, card)


        
        self.trunk = []
        self.hand = []

        self.health = 50

        self.selected_card = None
        self.drawn = False
        self.placed = False
