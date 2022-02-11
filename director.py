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
        ''' Create new variables for the class.
        '''
        self._correct_guess = True
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
        self._dictionary.display_word()
        self._jumper.display_chute()

    def _update_game(self):
        ''' Get new values from input user
        '''
        self._player._playerGuess()
        self._dictionary.update_word_display(self._player._playerGuess)
        self._correct_guess = self._dictionary.check_guess(self._player._playerGuess)
        if (self._correct_guess == False):
            self._jumper.update_lives(self._player._pastguess)
        else:
            pass

    def _end_game(self):
        ''' Decide whether the game is over according to # of lives
        '''
        self._lives = self._jumper.get_lives()
        if (self._lives == 0):
            return True
        else:
            return False