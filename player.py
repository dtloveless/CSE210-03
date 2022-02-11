'''
    File: player.py
    Author: Darcy Merilan
    Description:  The player class recieves the players guess and than
    storesthe past guesses from the player into a list
'''


class Player:

    def __init__(self):
        '''self._playerGuess()
        self._past_guess()''' 
        self._pastguesses = []
        self._player_guess = ''
    

    def get_player_guess(self):
        '''This ask the user to put in a 1 character
        guess into the code and stores that character
        for the dictionary to use'''
        self._player_guess = input("Guess a Letter [a-z]: ")
        #pc = playerchoice.lower
        return self._player_guess.lower()
        #needs to be limited to 1 letter

    def add_past_guess(self,oldguess):
        '''This list all the previous inputs that was 
        made by the player, and makes them unable to 
        use them going forward in the game.'''
        #need to be a list
        for letter in range(len(self._past_guess)):
            if(oldguess == self._past_guess[letter]):
                print('You have previously guessed this, try again.')
        return self._pastguesses.append
        