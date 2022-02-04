import random

words = ['vanish','health','parsimonious','support','kettle','beef','ajar','curious','imagine','shop']

class Dictionary:
    def __init__(self):
        self._current_word = random.choice(words)

    def get_word(self):
        return self._current_word

    def check_guess(self, playerGuess):
        for letter in self._current_word:
            if playerGuess == letter:
                return True
        return False

    def display_underscores(self):
        for x in range(len(self._current_word)):
            print('_ ', end= '')
        print('\n') #get an endline after the underscores


############### TEST CODE ##################
# test = Dictionary()
# print(f"Current Word: {test.get_word()}")
# test.display_underscores()

# print(test.check_guess('f'))
# print(test.check_guess('e'))
