import random
from state import Card
from settings import *

class FirstDealCommand():
    def __init__(self, state):

        self.state = state
        self.player_deck = state.player.deck
        self.computer_deck = state.computer.deck
        self.player_hand = state.player.hand
        self.computer_hand = state.computer.hand


    def run(self):

        random.shuffle(self.player_deck)
        random.shuffle(self.computer_deck)

        x1, y1 = HAND_PLAYER_LOCATION[0], HAND_PLAYER_LOCATION[1]
        x2, y2 = HAND_COMPUTER_LOCATION[0], HAND_COMPUTER_LOCATION[1]

        count = 7
        while count != 0:

            
            card = self.player_deck[0]
            card.state = 'hand'
            self.player_hand.insert(0, card)
            self.player_deck.remove(card)

            card = self.computer_deck[0]
            card.state = 'hand'
            self.computer_hand.insert(0, card)
            self.computer_deck.remove(card)
            count -= 1
