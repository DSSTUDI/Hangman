import random

# Contains the body of the hangman stage by stage in a list.
class Body:
    def __init__(self):
        stage1 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''
        stage2 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
        stage3 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
        stage4 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
        stage5 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
        stage6 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
        stage7 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
        self.the_body = [stage1, stage2, stage3, stage4, stage5, stage6, stage7]

        self.current_stage = -1

    # Returns the next stage of the body.
    def next_stage(self):
        self.current_stage = self.current_stage + 1
        return self.the_body[self.current_stage]


# Contains the list of all possible words for the game.
class Words:
    def __init__(self):
        self.words = ["acres", "adult", "advice", "attemp", "border", "brick", "breeze", "canal", "cast", "contrast",
                      "damage", "deep", "doll", "donkey", "face", "film", "movie", "cinema", "dinner", "garbage",
                      "garage", "grandmother", "habit", "image", "dance", "mathematics", "memory", "neighborhood",
                      "palace", "plate", "poetry", "positivity", "pride", "promise", "pedal", "relationship", "rock",
                      "rubber", "sale", "satellite", "horror", "selection", "smoothie", "skeleton", "sight", "slope"]

    # Returns a random word from the list.
    def get_word(self):
        return random.choice(self.words)


# Contains methods for main parts of the game.
# Also contains the list of already guessed letters.
class Game:
    def __init__(self):
        pass



    def start_game(self):
        self.new_word = Words.get_word()
        self.correct_letters = []
        self.wrong_letters = []
        for c in range(0, len(self.new_word)):
            print("_"),



    def guess_letter(self, letter):
        if letter in self.new_word:
            self.correct_letters.append(letter)
        else:
            self.wrong_letters.append(letter)





