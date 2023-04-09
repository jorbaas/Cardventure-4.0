import pygame


class DeckSprite(pygame.sprite.Sprite):
    def __init__(self, name, name_image, owner, loc, group):
        super().__init__(group)

        self.name = name
        self.owner = owner
        image = pygame.image.load(name_image)
        self.image = pygame.transform.scale(image, (100, 150))
        self.image.convert()
        self.rect = self.image.get_rect(center=loc)
        self.button_rect = self.rect.copy()

        self.highlighted = False

    # def update_image(self, new_image_file_path):
    #     image = pygame.image.load(new_image_file_path)
    #     self.image = pygame.transform.scale(image, (100, 150))
    #     self.image.convert()


    def highlight_deck(self, mouse_pos):
        """ If mouse is over the card move the card slightly up to highlight it """
        if self.button_rect.collidepoint(mouse_pos) and self.highlighted == False:
            self.rect.y -= 15
            self.rect.x -= 3
            self.highlighted = True

        elif not self.button_rect.collidepoint(mouse_pos) and self.highlighted == True:
            self.rect.y += 15
            self.rect.x += 3
            self.highlighted = False

    def update(self, mouse_pos):
        self.highlight_deck(mouse_pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
