from player import Player
from dictionary import Dictionary
from parachute import p

'''
    File: director.py
    Author: Celeste Popoca
    Despcription: Contains the director class of the game and 
'''

class Director:

    def __init__(self):
        # create new variables
        # pastGuesses = []
        # jumper = Jumper()
        # dictionary = Dictionary()
        # player = Player()
        pass

    def start_game(self):
        # while loop for playing the game
        while self._end_game():
            self._display_game()
            self._update_game()

    def _display_game(self):
        # beginning layout of the game
        # dictionary.displayUnderscores()
        # jumper.displayChute()

        pass

    def _update_game(self):
        # get new values
        # dictionary.checkGuess()
        # jumper.update_lives()
        pass

    def _end_game(self):
        # decide whether the game is over
        return False