from .Player import Player
import pygame

class CardGamestate():
    def __init__(self):

        # all sprite groups for the card game
        self.background_sprites = pygame.sprite.Group()
        self.button_sprites = pygame.sprite.Group()
        self.card_sprites = pygame.sprite.Group()
        self.deck_sprites = pygame.sprite.Group()

        # create players which contains the deck, health and turn checks etc
        self.player = Player('Jorbaas')
        self.computer = Player('Computer')

        # setup for "card holders" on the board
        self.monster_slot_1_player = []
        self.monster_slot_2_player = []
        self.middle_slot_1 = []
        self.middle_slot_2 = []
        self.monster_slot_1_computer = []
        self.monster_slot_2_computer = []

        # check if the battle phase has happened and for stacking cards
        self.battled = False



        self.turn_player = True

        # counter for turns, at two turns the battle phase starts and turn is reset to 0
        self.turn = 0


