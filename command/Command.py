import random
class Command():



    ##### SIMPLE GAME FUNCTIONS #####


    def shuffle_decks(self):
        random.shuffle(self.player_deck)
        random.shuffle(self.compter_deck)

    def draw_x_cards(hand, deck, x):
        count = x
        hand.insert(0, deck[0])
        deck.pop(0)
        count -= 1

    def first_card_on_pot(deck):
        pot = []
        pot.insert(0, deck[0])
        deck.pop(0)
        specials = ['-K', '-7', '-8', '-B', '-2', 'JOKER']
        while any(card in pot[0] for card in specials):
            draw_card(deck, pot)
            random.shuffle(deck)
            draw_card(pot, deck)







