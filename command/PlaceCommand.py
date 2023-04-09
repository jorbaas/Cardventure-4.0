
def PlaceCommand(state, player, sub_command):


    slot = sub_command

    # check if the player is allowed to place


    if player == 'player' and slot == 'slot_1' and not state.monster_slot_1_player:
        selected_card = state.player.selected_card


        # checks if the id's of the selected_card and a card in the hand matches
        # if so remove that card from the hand and insert into attack slot
        for card in state.player.hand:
            if card.values['id'] == selected_card.values['id']:


                card.state = 'placed_monster_slot_1_player'

                state.player.hand.remove(card)
                state.monster_slot_1_player.insert(0, card)
                state.player.selected_card = None


    elif player == 'player' and slot == 'slot_2' and not state.monster_slot_2_player:

        selected_card = state.player.selected_card

        # checks if the id's of the selected_card and a card in the hand matches
        # if so remove that card from the hand and insert into attack slot
        for card in state.player.hand:
            if card.values['id'] == selected_card.values['id']:

                card.state = 'placed_monster_slot_2_player'

                state.player.hand.remove(card)
                state.monster_slot_2_player.insert(0, card)
                state.player.selected_card = None






    elif player == 'computer' and state.computer.drawn == True:
        card = state.computer.selected_card
        state.monster_slot_1_computer.insert(0, card)
        state.computer.hand.remove(card)






