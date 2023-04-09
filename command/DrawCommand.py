
def drawCommand(state, player):

    """ Checks if the player or computer is allowed to draw,
         and draws a card if so. """

    player_deck = state.player.deck
    computer_deck = state.computer.deck
    player_hand = state.player.hand
    computer_hand = state.computer.hand
    player_drawn = state.player.drawn
    computer_drawn = state.computer.drawn


    if player == 'player' and player_drawn == False:
        card = state.player.deck[0]
        card.state = 'drawn'
        state.player.hand.insert(0, state.player.deck.pop(0))
        # state.player.drawn = True



    elif player == 'computer' and computer_drawn == False:
        card = state.computer.deck[0]
        card.state = 'drawn'

        state.computer.hand.insert(0, state.computer.deck.pop(0))






