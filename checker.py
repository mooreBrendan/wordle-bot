from bot import Bot
from copy import copy
from random import randint


class Checker(Bot):
  def __init__(self, file):
    super().__init__(file)
    self.full_words = copy(self.words)

    # get length of words (for easily doing longer wordles)
    self.length = len(self.full_words[0])

  def evaluate(self, guess, answer):
    pattern = "_"*self.length
    temp = ""
    for index, element in enumerate(answer):
      if guess[index] == element:
        pattern[index] = "x"
      else:
        temp += element

    for index, element in enumerate(guess):
      if element in temp:
        pattern[index] = "o"

    return pattern

  def test_game(self):
    answer = self.full_words[randint(0, len(self.full_words))]
    guess = "TODO:"
    pattern = self.evaluate(guess, answer)
