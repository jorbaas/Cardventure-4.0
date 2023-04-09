import pygame

class BackgroundSprite(pygame.sprite.Sprite):
    def __init__(self, name, image_name, loc, group):
        super().__init__(group)

        self.name = name

        image = pygame.image.load('assets/background_images/' + image_name)
        self.image = image.convert_alpha()

        self.rect = self.image.get_rect(center=loc)




        arrow_image = pygame.image.load('assets/background_images/arrow_down_image.png')
        arrow_image = pygame.transform.scale(arrow_image, (120, 120))
        self.arrow_image = arrow_image.convert_alpha()
        self.arrow_rect = self.arrow_image.get_rect(center=loc)
        self.original_arrow_rect = self.arrow_rect.copy()

        self.move_arrow_direction = 'down'



    def rotate_image(self):
        if 'monster_slot_1_computer' or 'monster_slot_2_computer' in self.name:
            self.image = pygame.transform.rotate(self.image, 180)


    def move_place_arrow(self):
        """ Moves arrow up and down """

        arrow_speed = 1

        if self.move_arrow_direction == 'down':
            self.arrow_rect.y += arrow_speed
            if self.arrow_rect.y == self.original_arrow_rect.y + 10:
                self.move_arrow_direction = 'up'

        elif self.move_arrow_direction =='up':
            self.arrow_rect.y -= arrow_speed
            if self.arrow_rect.y == self.original_arrow_rect.y - 10:
                self.move_arrow_direction = 'down'

        else:
            self.arrow_rect.y -= arrow_speed


    def update(self):
        self.move_place_arrow()


    def draw(self, screen, state):
        screen.blit(self.image, self.rect)

        # only shows the place arrow above the player slots if a card is clicked
        if self.name == 'monster_slot_1_player' or self.name == 'monster_slot_2_player':
            for sprite in state.card_sprites:
                if sprite.clicked and sprite.state == 'hand':
                    screen.blit(self.arrow_image, self.arrow_rect)

        elif self.name == 'middle_slot_1':
            for sprite in state.card_sprites:
                if sprite.clicked and sprite.state == 'placed_monster_slot_1_player':
                    screen.blit(self.arrow_image, self.arrow_rect)

        elif self.name == 'middle_slot_2':
            for sprite in state.card_sprites:
                if sprite.clicked and sprite.state == 'placed_monster_slot_2_player':
                    screen.blit(self.arrow_image, self.arrow_rect)









