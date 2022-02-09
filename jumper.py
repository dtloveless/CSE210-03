"""
File: jumper.py
Author: Daniel Loveless
Class: CSE210, BYU-I
Description:
    Holds class with attribute for # of lives used and methods to update 
    _lives_used value and display the ASCII parachute graphic according to this
    value.
"""

class Jumper():
    def __init__(self):
        self.__parachute__ = [
            '  ___',
            ' /___\\',
            ' \   /',
            '  \ /',
            '   O',
            '  /|\\',
            '  / \\',
        ]
        self._lives_used = 0
    
    def update_lives(self, guesses_used):
        """Updates local value for lives used based on length of guesses list.
        Args:
            guesses_used ([list]): list of incorrect guesses attempted by player
        """
        self._lives_used = len(guesses_used)
        
    def display_chute(self):
        """Displays ASCII graphic for jumper w/parachute according to how many
        lives are remaining.
        """
        print()
        # Condition for no lives remaining: displays dead jumper
        if self._lives_used > 3:
            for i in range(4):
                print()
            print('   x')
            for i in range(5, 7):
                print(self.__parachute__[i])
        # Displays jumper and parachute w/layers missing according to # of lives
        # used
        elif self._lives_used > 0:
            for i in range(self._lives_used):
                print()
            for i in range(self._lives_used, 7):
                print(self.__parachute__[i])
        # Condition for full health: simply displays full jumper graphic
        else:
            for line in self.__parachute__:
                print(line)
        print('\n^^^^^^^')
        
    def get_lives(self):
        ''' Passes the number of lives in the protected variable 'lives_used'
        '''
        return self._lives_used