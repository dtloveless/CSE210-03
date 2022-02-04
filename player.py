class Player:

    def __init__(self):
        self._playerGuess()
        self._past_guess()
    

    def _playerGuess(self,playerchoice):
        '''This ask the user to put in a 1 character
        guess into the code and stores that character
        for the dictionary to use'''
        playerchoice = input("Guess a Letter [a-z]: ")
        pc = playerchoice.lower
        return pc
        #needs to be limited to 1 letter

    def _past_guess():
        '''This list all the previous inputs that was 
        made by the player, and makes them unable to 
        use them going forward in the game.'''
        pass