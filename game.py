from bot import Bot
from copy import copy
from random import randrange


def string_set(string, index, char):
  return string[:index] + char + string[index+1:]


class Game(Bot):
  def __init__(self, file, num_guesses):
    super().__init__(file)
    self.full_words = copy(self.words)

    # get length of words (for easily doing longer wordles)
    self.length = len(self.full_words[0])
    self.num_guesses = num_guesses

  def evaluate(self, guess, answer):
    pattern = "_"*self.length
    temp = ""
    for index, element in enumerate(answer):
      if guess[index] == element:
        pattern = string_set(pattern, index, "x")
        temp += guess[index]

    for index, element in enumerate(answer):
      if pattern[index] != "x" and guess[index] in answer:
        letter = guess[index]
        if temp.count(letter) < answer.count(letter):
          pattern = string_set(pattern, index, "o")
          temp += guess[index]
    return pattern

  def test_game(self, print_d=False):
    rounds = []
    answer = copy(self.full_words[randrange(0, len(self.full_words))])
    self.words = copy(self.full_words)
    if print_d:
      print(f"{answer=}")
    for _ in range(self.num_guesses):
      guess = self.get_word()
      pattern = self.evaluate(guess, answer)
      rounds.append([copy(guess), copy(pattern)])
      if print_d:
        print(f"{rounds[_]}")
      if pattern == "x"*self.length:
        if print_d:
          print(rounds)
        return rounds
      self.words = self.cull_list(guess, pattern)

    if print_d:
      print(rounds)
    return rounds
