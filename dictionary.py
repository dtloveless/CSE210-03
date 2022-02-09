'''
File: dictionary.py
Author: Julie Cowley
Class: CSE 210
Description: generates a random word for the game
'''

import random


class Dictionary:

    def __init__(self):
        words = ['vanish','health','parsimonious','support','kettle','beef','ajar','curious','imagine','shop']
        self._current_word = random.choice(words)

        # fill up the word display with underscores at first
        self.wordDisplay = []
        for x in range(len(self._current_word)):
            self.wordDisplay.append('_')

    def get_word(self):
        '''
        Returns the current word
        '''
        return self._current_word

    def check_guess(self, playerGuess):
        '''
        recieves a letter 
        returns true if the letter is in the current word, false otherwise
        '''
        for letter in self._current_word:
            if playerGuess == letter:
                return True
        return False

    def display_word(self):
        '''
        displays the underscores and letters of the current word 
        '''
        for letter in range(len(self._current_word)):
            print(f"{self.wordDisplay[letter]} ", end='')

    def update_word_display(self, playerGuess):
        '''
        updates the word display with the player's guess
        '''
        for letter in range(len(self._current_word)):
            if(playerGuess == self._current_word[letter]):
                self.wordDisplay[letter] = playerGuess



test = Dictionary()
print(test.get_word())
test.display_word()
test.update_word_display('a')
test.display_word()
