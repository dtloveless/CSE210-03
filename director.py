from player import Player
from dictionary import Dictionary
from jumper import Jumper

'''
    File: director.py
    Author: Celeste Popoca
    Description: Contains the director class of the game and executes the 
    other classes' modules.
'''

class Director:

    def __init__(self):
        '''create new variables'''
        self._guess_list = []
        self._lives = -1
        self._jumper = Jumper()
        self._dictionary = Dictionary()
        self._player = Player()
        pass

    def start_game(self):
        ''' Play the game while there are lives available
        '''
        while self._end_game():
            self._display_game()
            self._update_game()

    def _display_game(self):
        ''' Display layout of the game with the word and parachute
        '''
        self._dictionary.displayUnderscores()
        self._jumper.displayChute()

    def _update_game(self):
        ''' Get new values from input user
        '''
        self._dictionary.check_guess()
        self._jumper.update_lives()

    def _end_game(self):
        ''' Decide whether the game is over according to # of lives
        '''
        self._lives = self._jumper.get_lives()
        if (self._lives == 0):
            return True
        else:
            return False