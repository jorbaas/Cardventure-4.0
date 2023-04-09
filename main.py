import pygame
from mode import CardGame
from settings import *


class UserInterface():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Cardventure 4.0')

        self.active_mode = 'CardGame'
        self.card_game_mode = CardGame.CardGame()


        self.clock = pygame.time.Clock()
        self.running = True


    def run(self):
        while self.running:
            if self.active_mode == 'CardGame':
                self.card_game_mode.run(self.screen)

            # Update display
            pygame.display.update()
            self.clock.tick(30)


user_interface = UserInterface()
user_interface.run()

