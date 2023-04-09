
import pygame
from settings import *


class CardSprite(pygame.sprite.Sprite):
    def __init__(self, card, owner, loc, group):
        super().__init__(group)


        card_values = card.values

        self.loc = loc

        # state can be hand, deck, placed etc.
        # depending on the state the card behaves differently
        self.state = card.state
        self.slot = 0

        self.name = card_values['name']
        self.id = card_values['id']
        self.description = card_values['description']
        self.attack = card_values['attack']
        self.defense = card_values['defense']

        name_monster_image = card_values['name_image']
        name_card_template = card_values['name_card']

        self.owner = owner

        # if cards are from the computer, switch the images to show the back
        if owner == 'computer':
            card_image = pygame.image.load('assets/PNG-cards/back.png')
            monster_image = pygame.image.load('assets/PNG-cards/back.png')
            card_image = pygame.transform.scale(card_image, (100, 150))
            monster_image = pygame.transform.scale(monster_image, (100, 150))
        # shows the card if is player cards
        else:
            card_image = pygame.image.load('assets/card_templates/' + name_card_template)
            monster_image = pygame.image.load('assets/card_images/' + name_monster_image)

        # for performance and transparency
        card_image.convert_alpha()
        monster_image.convert_alpha()

        # merge the card template and the image to one image
        width = max(card_image.get_width(), monster_image.get_width())
        height = max(card_image.get_height(), monster_image.get_height())
        merged_image = pygame.Surface((width, height), pygame.SRCALPHA)
        merged_image.blit(monster_image, (0, 0))
        merged_image.blit(card_image, (0, 0))
        self.image = merged_image

        # list for the text surfaces for the description
        self.desc_surfaces = []

        self.rect = self.image.get_rect(center=loc)
        self.button_rect = self.rect.copy()

        self.highlighted = False
        self.clicked = False

        # creates the text for the card
        self.set_name()
        self.set_description()
        self.set_att_def()


    def set_description(self):
        """ Gets called in the innit, sets the surface description of the card,
            gets drawn in the draw method. """

        # set the description attribute
        text = self.description

        # list of the text surfaces [surface, (x,y)]
        self.text_description = []

        font = pygame.font.SysFont('Arial', 7)

        # splits the description into words and lines.
        self.words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        self.space = font.size(' ')[0]  # The width of a space.


        for line in self.words:
            for word in line:
                desc_surface = font.render(word, 0, BLACK)
                self.desc_surfaces.append(desc_surface)


    def set_name(self):
        """ creates surface for the card name """

        # blit name on card
        font_name = pygame.font.SysFont('Arial', 11)
        self.name_surface = font_name.render(self.name, 0, BLACK)

    def set_att_def(self):
        """ creates surface for the card attack and defense values. """

        font_name = pygame.font.SysFont('Arial', 10)
        self.attack_surface = font_name.render(str(self.attack), 0, BLACK)
        self.defense_surface = font_name.render(str(self.defense), 0, BLACK)

    def highlight_card(self, mouse_pos, mouse_clicked):
        """ If mouse is over the card move the card slightly up to highlight it """

        if self.owner == 'player':
            if self.button_rect.collidepoint(mouse_pos) and self.highlighted == False:
                self.rect.y -= 15
                self.rect.x -= 3
                self.highlighted = True

            # elif not self.button_rect.collidepoint(mouse_pos) and self.highlighted == True:
            elif self.highlighted and not self.clicked and not self.button_rect.collidepoint(mouse_pos):
                self.rect.y += 15
                self.rect.x += 3
                self.highlighted = False


    def clicked_card(self, mouse_pos, mouse_clicked):

        if self.owner == 'player':
            if self.button_rect.collidepoint(mouse_pos) and mouse_clicked:
                self.clicked = True
                print('clicked '+ self.name)
            elif not self.button_rect.collidepoint(mouse_pos) and mouse_clicked:
                self.clicked = False


    # def update_sprites(self, state):

    def move_to_monster_slot(self):
        if self.state == 'placed_monster_slot_1_player':
            # if self.rect != self.image.get_rect(center=MONSTER_SLOT_1_PLAYER_LOCATION):
            self.rect = self.image.get_rect(center=MONSTER_SLOT_1_PLAYER_LOCATION)
            self.button_rect = self.rect.copy()
            self.slot = 1


        elif self.state == 'placed_monster_slot_2_player':
            # if self.rect != self.image.get_rect(center=MONSTER_SLOT_2_PLAYER_LOCATION):
            self.rect = self.image.get_rect(center=MONSTER_SLOT_2_PLAYER_LOCATION)
            self.button_rect = self.rect.copy()
            self.slot = 2



    def update(self, mouse_pos, mouse_clicked, state):

        # update the card state


        if self.state == 'hand':

            self.clicked_card(mouse_pos, mouse_clicked)
            self.highlight_card(mouse_pos, mouse_clicked)

        elif self.slot == 0:
            self.move_to_monster_slot()
            self.highlighted = False
            self.clicked = False

        elif self.state == 'placed_middle_slot_1':


            # if self.rect != self.image.get_rect(center=MONSTER_SLOT_2_PLAYER_LOCATION):
            self.rect = self.image.get_rect(center=MIDDEL_SLOT_1_LOCATION)
            self.button_rect = self.rect.copy()
            self.slot = 3


        elif self.state == 'placed_middle_slot_2':
            # if self.rect != self.image.get_rect(center=MONSTER_SLOT_2_PLAYER_LOCATION):
            self.rect = self.image.get_rect(center=MIDDEL_SLOT_2_LOCATION)
            self.button_rect = self.rect.copy()
            self.slot = 4



        elif self.state == 'placed_monster_slot_1_player' or self.state == 'placed_monster_slot_2_player':
            self.clicked_card(mouse_pos, mouse_clicked)



        # elif self.rect == self.image.get_rect(center=MONSTER_SLOT_1_PLAYER_LOCATION) \
        #         or self.rect == self.image.get_rect(center=MONSTER_SLOT_2_PLAYER_LOCATION):
        #     self.clicked_card(mouse_pos, mouse_clicked)
        #     self.highlight_card(mouse_pos, mouse_clicked)
        #     print('test')



    def draw(self, screen):
        """ Draw the sprite onto the given surface
        with text ontop """

        # check if the card is visible
        if self.state != 'covered':
            # first, blit the card image onto the surface
            screen.blit(self.image, self.rect)


            # second, draw the name on the image if it is the player card
            if self.owner == 'player':
                x, y = self.rect.x, self.rect.y
                x += 18
                screen.blit(self.name_surface, (x, y))

                # third, blit the att and def values on the card
                x, y = self.rect.x, self.rect.y
                x += 5
                y_attack = y + 18
                y_defense = y + 35

                screen.blit(self.attack_surface, (x, y_attack))
                screen.blit(self.defense_surface, (x, y_defense))

                # last, blit the description
                x, y = self.rect.x, self.rect.y
                x += 18
                y += 100

                for surface in self.desc_surfaces:
                    max_width, max_height = x + 30, y + 50
                    word_width, word_height = surface.get_size()

                    # print(x + word_width, max_width)
                    if x + word_width >= max_width:
                        x = self.rect.x  # Reset the x.
                        x += 18
                        y += word_height  # Start on new row.

                    screen.blit(surface, (x, y))

                    x += word_width + self.space


            # Finally, update the sprite's `dirty` attribute so that it gets redrawn
            self.dirty = 1

