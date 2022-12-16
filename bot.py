from string import ascii_lowercase


class Bot:
  def __init__(self, file, print_d=False):
    self.words = self.get_words(file)
    self._print = print_d

  def get_words(self, fname):
    file = open(fname)
    words = file.read().split("\n")
    return words

  def check_move(self, letter, index, word):
    cleaned = word[:index]+word[index+1:]
    return letter in cleaned

  def check_doubles(self, new_guess, pattern):
    temp = []
    for i, e in enumerate(new_guess):
      if pattern[i] == "x":
        continue
      elif pattern[i] == "o":
        continue
      temp.append(e)
    return temp

  def check(self, prev_guess, pattern, new_guess):
    for index, pat in enumerate(pattern):
      if pat == "_":
        temp = self.check_doubles(new_guess, pattern)
        if prev_guess[index] in temp:
          return False
      elif pat == "o":
        # check for difference
        if new_guess[index] == prev_guess[index]:
          return False
        if not self.check_move(prev_guess[index], index, new_guess):
          return False
      elif pat == "x":
        if new_guess[index] != prev_guess[index]:
          return False

    return True

  def cull_list(self, prev_guess, pattern):
    return [i for i in self.words if self.check(prev_guess, pattern, i)]

  def prompt(self):
    x = input("enter word:")
    y = input(
        "enter pattern ('_' = not in word, 'o' = wrong spot, 'x'=correct:")
    return x, y

  def check_input(self, guess, pattern):
    if (len(guess) != 5):
      return False
    if (len(pattern) != 5):
      return False
    for i in guess.lower():
      if i not in ascii_lowercase:
        return False
    for i in pattern.lower():
      if i not in ["_", "o", "x"]:
        return False
    return True

  def get_input(self):
    cond = False
    while not cond:
      guess, pattern = self.prompt()
      cond = self.check_input(guess, pattern)
    return guess, pattern

  def get_word(self):
    if len(self.words) < 1:
      raise ValueError("WORD LIST EMPTY!!!!")
    return self.words[0]

  def run(self):
    for _ in range(6):
      word_choie = self.get_word()
      if self._print:
        print(f"word space:{len(self.words)}")
        print(word_choie)
      if len(self.words) == 1 and self._print:
        print("FINAL ANSWER")
        return
      guess, pattern = self.get_input()
      if pattern == "xxxxx" and self._print:
        print("congratulations!")
        return
      self.words = self.cull_list(guess, pattern)

    if self._print:
      print("failed game")
