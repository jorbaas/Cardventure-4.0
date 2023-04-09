from settings import *
from sprite import *
import sprite
from state import Card


def make_background(group):
    BackgroundSprite('background', 'background_black.png', (640, 450), group)
    BackgroundSprite('monster_slot_1_player', 'card_zone.png', MONSTER_SLOT_1_PLAYER_LOCATION, group)
    BackgroundSprite('monster_slot_2_player', 'card_zone.png', MONSTER_SLOT_2_PLAYER_LOCATION, group)
    BackgroundSprite('monster_slot_1_computer', 'card_zone.png', MONSTER_SLOT_1_COMPUTER_LOCATION, group).rotate_image()
    BackgroundSprite('monster_slot_2_computer', 'card_zone.png', MONSTER_SLOT_2_COMPUTER_LOCATION, group).rotate_image()
    BackgroundSprite('middle_slot_1', 'middel_ground_image.png', MIDDEL_SLOT_1_LOCATION, group)
    BackgroundSprite('middle_slot_2', 'middel_ground_image.png', MIDDEL_SLOT_2_LOCATION, group)


    # BackgroundSprite('stats_bar_player', 'player_stats_bar.png', PLAYER_STATS_BAR_LOCATION, group)
    # BackgroundSprite('stats_bar_computer', 'player_stats_bar.png', COMPUTER_STATS_BAR_LOCATION, group)

def make_buttons(group):
    ButtonSprite(END_TURN_BUTTON, group)




def make_hand_sprites(state):
    """ Creates the player sprites for the player's and computer's hands
        and adds them to the sprite groups """

    x1, y1 = HAND_PLAYER_LOCATION[0], HAND_PLAYER_LOCATION[1]
    x2, y2 = HAND_COMPUTER_LOCATION[0], HAND_COMPUTER_LOCATION[1]

    for card in state.player.hand:
        # CardSprite(card, ('PNG-cards/' + card + '.png'), 'player', (x1, y1), state.card_sprites)
        CardSprite(card, 'player', (x1, y1), state.card_sprites)
        # Card(card['name'], 'player', card['name_card'], card['name_image'], (x1, y1), state.card_sprites)
        x1 += 100
    for card in state.computer.hand:
        CardSprite(card, 'computer', (x2, y2), state.card_sprites)

        # CardSprite(card, ('PNG-cards/' + card + '.png'), 'computer', (x2, y2), state.card_sprites)
        x2 += 100

def update_card_sprite_state(state):

    # creates a card sprite if the player draws a card
    for card in state.player.hand:
        if card.state == 'drawn':
            card.state = 'hand'
            CardSprite(card, 'player', (HAND_PLAYER_LOCATION), state.card_sprites)
            reset_card_spacing(state, 'player')


       # updates the sprite state to the card states in the attack slot
    for card in state.monster_slot_1_player:
        for sprite in state.card_sprites:
            if card.values['id'] == sprite.id and card.state != sprite.state:
                sprite.state = card.state
                reset_card_spacing(state, 'player')

    # updates the sprite state to the card states in the attack slot
    for card in state.monster_slot_2_player:
        for sprite in state.card_sprites:
            if card.values['id'] == sprite.id and card.state != sprite.state:
                sprite.state = card.state
                reset_card_spacing(state, 'player')


    for card in state.middle_slot_1:
        for sprite in state.card_sprites:
            if card.values['id'] == sprite.id and card.state != sprite.state:
                sprite.state = card.state






    # creates a card sprite if the computer draws a card
    for card in state.computer.hand:

        if card.state == 'drawn':
            print('WOROSK')
            card.state = 'hand'
            CardSprite(card, 'computer', (HAND_COMPUTER_LOCATION), state.card_sprites)
            reset_card_spacing(state, 'computer')



    # updates the sprite state to the card states in the attack slot
    for card in state.monster_slot_1_computer:
        for sprite in state.card_sprites:
            if card.values['id'] == sprite.id and card.state != sprite.state:
                sprite.state = card.state
                reset_card_spacing(state, 'computer')


    # updates the sprite state to the card states in the attack slot
    for card in state.monster_slot_2_computer:
        for sprite in state.card_sprites:
            if card.values['id'] == sprite.id and card.state != sprite.state:
                sprite.state = card.state
                reset_card_spacing(state, 'computer')


def reset_card_spacing(state, player):
    """ Resets the spacing of the cards in the hand """
    x_player, y_player = HAND_PLAYER_LOCATION[0], HAND_PLAYER_LOCATION[1]
    x_computer, y_computer = HAND_COMPUTER_LOCATION[0], HAND_COMPUTER_LOCATION[1]

    group = state.card_sprites
    player_hand = state.player.hand
    computer_hand = state.computer.hand
    # determine the card spacing based on amount of cards

    if player == 'player':
    
        if len(player_hand) > 7:
            card_spacing = 700 / len(player_hand)
    
        else:
            card_spacing = 100
    
        # set the position of each card in the hand
        for sprite in group:
            if sprite.owner == 'player' and sprite.state == 'hand':
    
                # scales the button width by card_spacing
                sprite.button_rect.w = card_spacing
                # subtracts half the card width from the x
                sprite.button_rect.x = x_player - 50
                sprite.pos = (x_player, y_player)
    
                sprite.rect = sprite.image.get_rect(center=sprite.pos)
                # sprite.rect_button = sprite.image.get_rect(center=sprite.pos)
                x_player += card_spacing
    
    elif player == 'computer':
        if len(computer_hand) > 7:
            card_spacing = 700 / len(computer_hand)

        else:
            card_spacing = 100

            # set the position of each card in the hand
        for sprite in group:
            if sprite.owner == 'computer' and sprite.state == 'hand':
                # scales the button width by card_spacing
                sprite.button_rect.w = card_spacing
                # subtracts half the card width from the x
                sprite.button_rect.x = x_computer - 50
                sprite.pos = (x_computer, y_computer)

                sprite.rect = sprite.image.get_rect(center=sprite.pos)
                # sprite.rect_button = sprite.image.get_rect(center=sprite.pos)
                x_computer += card_spacing
        


