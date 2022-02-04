from player import Player 
'''
    Authors: Daniel Loveless, Julie Cowley, 
        Celeste Popoca, Darcy Merilan
'''

class Director:

    def __init__(self):
        # create new variables
        pass

    def start_game(self):
        # while loop for playing the game
        while self._end_game():
            self._display_game()
            self._update_game()

    def _display_game(self):
        # beginning layout of the game
        pass

    def _update_game(self):
        # get new values
        pass

    def _end_game(self):
        # decide whether the game is over
        return False