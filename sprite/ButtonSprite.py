import pygame

class ButtonSprite(pygame.sprite.Sprite):
    def __init__(self, button, group):
        super().__init__(group)

        self.state = 'idle'

        self.name = button['name']
        self.type = button['type']
        self.name_image = button['name_image']
        self.name_selected_image = button['name_selected_image']
        self.loc = button['location']

        self.image = pygame.image.load('assets/buttons/' + self.name_image)
        self.image.convert_alpha()

        self.rect = self.image.get_rect(center=self.loc)



    def change_image(self, mouse_pos, mouse_clicked):
        if self.rect.collidepoint(mouse_pos) and mouse_clicked:
            if self.state == 'idle':
                self.image = pygame.image.load('assets/buttons/' + self.name_selected_image)
                self.state = 'selected'

        if not self.rect.collidepoint(mouse_pos) and mouse_clicked:
            if self.state == 'selected':
                self.image = pygame.image.load('assets/buttons/' + self.name_image)
                self.state = 'idle'


    def update(self, mouse_pos, mouse_clicked):
        self.change_image(mouse_pos, mouse_clicked)


    def draw(self, screen):
        screen.blit(self.image, self.rect)

