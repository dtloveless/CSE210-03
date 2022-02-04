import random


class Dictionary:
    '''
    generates a random word for the game
    '''

    def __init__(self):
        words = ['vanish','health','parsimonious','support','kettle','beef','ajar','curious','imagine','shop']
        self._current_word = random.choice(words)

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

    def display_underscores(self):
        '''
        displays underscores for each letter in the current word
        '''
        for x in range(len(self._current_word)):
            print('_ ', end= '')
        print('\n') #get an endline after the underscores finish printing


############### TEST CODE ##################
# test = Dictionary()
# print(f"Current Word: {test.get_word()}")
# test.display_underscores()

# print(test.check_guess('f'))
# print(test.check_guess('e'))
