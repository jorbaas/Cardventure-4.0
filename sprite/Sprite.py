import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, name_image, owner, group):
        super().__init__(group)
        self.image = pygame.image.load(name_image)

        self.owner = owner


    def renderSprite(self):
        pass