import pygame
import sys
from settings import *
from state import CardGamestate, Card, H_2
from sprite import DeckSprite
from .GameMode import GameMode
from command import *


class CardGame(GameMode):
    """ called in the main.py.
        Creates an instance of CardGamestate which contains all the game objects and variables
        Processes input
        updates the sprites accordingly. """

    def __init__(self):
        super().__init__()

        self.game_state = CardGamestate()
        self.mouse_clicked = False

        # command can be: 'draw', 'place', 'end_turn', etc.
        self.commands = []
        self.sub_command = None

        self.setup()

    def setup(self):

        # load background sprites
        make_background(self.game_state.background_sprites)

        # load button sprites
        make_buttons(self.game_state.button_sprites)

        # deals the first turn
        first_deal = FirstDealCommand(self.game_state)
        first_deal.run()

        # makes the sprites of the hands
        make_hand_sprites(self.game_state)
        DeckSprite('deck', 'assets/PNG-cards/back.png', 'player', DECK_PLAYER_LOCATION, self.game_state.deck_sprites)
        DeckSprite('deck', 'assets/PNG-cards/back.png', 'computer', DECK_COMPUTER_LOCATION, self.game_state.deck_sprites)

    def process_input(self):
        """ Processes the raw input into commands ands ads them to the command list. """
        # gets the raw input
        self.mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    break

            # player can only give further input if it is his turn
            if self.game_state.turn_player:

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_clicked = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_clicked = False

            # checks if the player clicks on things

                # deck
                for sprite in self.game_state.deck_sprites:
                    if sprite.button_rect.collidepoint(self.mouse_pos) and self.mouse_clicked:
                        print("deck clicked")
                        print("jor is een sukkel")
                        self.commands.append('draw')
                        self.mouse_clicked = False
                        break


                # click a card on the screen
                for sprite in self.game_state.card_sprites:
                    if sprite.button_rect.collidepoint(self.mouse_pos)\
                            and sprite.clicked == True:



                        # saves a place command and the selected card
                        for card in self.game_state.player.hand:
                            values = card.values
                            if values['id'] == sprite.id:
                                self.game_state.player.selected_card = card
                                # self.commands.append('place')
                                self.mouse_clicked = False
                                break

                        # saves selected card in monster zone
                        for card in self.game_state.monster_slot_1_player:
                            if card.values['id'] == sprite.id:
                                self.game_state.player.selected_card = card
                                self.mouse_clicked = False

                                break


                        self.mouse_clicked = False



                # select spot to place card
                for sprite in self.game_state.background_sprites:
                    if sprite.rect.collidepoint(self.mouse_pos) and self.mouse_clicked:

                        if sprite.name == 'monster_slot_1_player':
                            if self.mouse_clicked and self.game_state.player.selected_card:
                                self.commands.append('place')
                                self.sub_command = 'slot_1'
                                break

                        elif sprite.name == 'monster_slot_2_player':
                            if self.mouse_clicked and self.game_state.player.selected_card:
                                self.commands.append('place')
                                self.sub_command = 'slot_2'
                                break

                        elif sprite.name == 'middle_slot_1':

                            if self.mouse_clicked and self.game_state.player.selected_card:
                                self.commands.append('move')
                                self.sub_command = 'slot_3'

                                break

                        elif sprite.name == 'middle_slot_2':
                            if self.mouse_clicked and self.game_state.player.selected_card:
                                self.commands.append('move')
                                self.sub_command = 'slot_4'
                                break




                # buttons
                for sprite in self.game_state.button_sprites:
                    if sprite.rect.collidepoint(self.mouse_pos)\
                            and self.mouse_clicked\
                            and sprite.state == 'selected':
                            print('turn ended')
                            self.game_state.turn_player = False
                            break



    def computer_turn(self):

        if not self.game_state.turn_player:
            drawCommand(self.game_state, 'computer')
            # PlaceCommand(self.game_state, 'computer')
            self.game_state.turn_player = True



    def send_commands(self):

        for command in self.commands:
            if command == 'draw':
                drawCommand(self.game_state, 'player')
                self.commands.remove(command)

            elif command == 'place':
                # sub command is the slot
                PlaceCommand(self.game_state, 'player', self.sub_command)
                self.commands.remove(command)
                self.sub_command = None

            elif command == 'move':

                MoveCommand(self.game_state, 'player', self.sub_command)
                self.commands.remove(command)
                self.sub_command = None



    def general_update(self):

        # resets the selected card of the player if it is not clicked anymore
        if self.game_state.player.selected_card:
            if not any(sprite.clicked for sprite in self.game_state.card_sprites if
                       sprite.name == self.game_state.player.selected_card.values['name']):
                self.game_state.player.selected_card = None

    def update_sprites(self):
        """ Updates sprite group to current game state,
            and to check if a card is highlighted. """

        self.game_state.background_sprites.update()

        self.game_state.button_sprites.update(self.mouse_pos, self.mouse_clicked)


        update_card_sprite_state(self.game_state)
        self.game_state.card_sprites.update(self.mouse_pos, self.mouse_clicked, self.game_state)
        self.game_state.deck_sprites.update(self.mouse_pos)


    def render(self, screen):

        for sprite in self.game_state.background_sprites:
            sprite.draw(screen, self.game_state)

        # self.game_state.background_sprites.draw(screen)


        self.game_state.button_sprites.draw(screen)

        self.game_state.deck_sprites.draw(screen)


        highlighted_sprite = []
        for sprite in self.game_state.card_sprites:
            if sprite.state == 'hand':
                if sprite.highlighted:
                    highlighted_sprite.append(sprite)
                    continue

                sprite.draw(screen)
            else:
                sprite.draw(screen)
            # elif sprite.state == 'placed_monster_slot_1_player':
            #     sprite.draw(screen)
            # elif sprite.state == 'placed_monster_slot_2_player':
            #     sprite.draw(screen)

        # renders highlighted sprite last
        if highlighted_sprite:
            for sprite in highlighted_sprite:
                sprite.draw(screen)



    def run(self, screen):
        self.process_input()
        self.computer_turn()
        self.send_commands()
        self.general_update()
        self.update_sprites()
        self.render(screen)




        #