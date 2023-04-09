
def MoveCommand(state, player, subcommand):

    slot = subcommand

    if player == 'player' and slot == 'slot_3' and not state.middle_slot_1:
        selected_card = state.player.selected_card

        for card in state.monster_slot_1_player:
            print(str(card.values['name'])+ '   ' + str(selected_card.values['name']))
            if card.values['id'] == selected_card.values['id']:

            # checks if the id's of the selected_card and a card in the hand matches
            # if so remove that card from the hand and insert into attack slot

                selected_card.state = 'placed_middle_slot_1'

                state.monster_slot_1_player.remove(selected_card)
                state.middle_slot_1.insert(0, selected_card)
                state.player.selected_card = None
