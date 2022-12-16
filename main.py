from string import ascii_lowercase


def get_words():
  file = open("valid-wordle-words.txt")
  words = file.read().split("\n")
  return words


# pattern: __ox_
def check_move(letter, index, word):
  cleaned = word[:index]+word[index+1:]
  return letter in cleaned


def check_doubles(new_guess, pattern):
  temp = []
  for i, e in enumerate(new_guess):
    if pattern[i] == "x":
      continue
    elif pattern[i] == "o":
      continue
    temp.append(e)
  return temp


def check(prev_guess, pattern, new_guess):
  for index, pat in enumerate(pattern):
    if pat == "_":
      temp = check_doubles(new_guess, pattern)
      if prev_guess[index] in temp:
        return False
    elif pat == "o":
      # check for difference
      if new_guess[index] == prev_guess[index]:
        return False
      if not check_move(prev_guess[index], index, new_guess):
        return False
    elif pat == "x":
      if new_guess[index] != prev_guess[index]:
        return False

  return True


def cull_list(words, prev_guess, pattern):
  return [i for i in words if check(prev_guess, pattern, i)]


def prompt():
  x = input("enter word:")
  y = input("enter pattern ('_' = not in word, 'o' = wrong spot, 'x'=correct:")
  return x, y


def check_input(guess, pattern):
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


def get_input():
  cond = False
  while not cond:
    guess, pattern = prompt()
    cond = check_input(guess, pattern)
  return guess, pattern


def get_word(words):
  if len(words) < 1:
    raise ValueError("WORD LIST EMPTY!!!!")
  return words[0]


def run_bot(words, print_d=False):
  for _ in range(6):
    word_choie = get_word(words)
    if print_d:
      print(f"word space:{len(words)}")
      print(word_choie)
    if len(words) == 1 and print_d:
      print("FINAL ANSWER")
      return
    guess, pattern = get_input()
    if pattern == "xxxxx" and print_d:
      print("congratulations!")
      return
    words = cull_list(words, guess, pattern)

  if print_d:
    print("failed game")


if __name__ == "__main__":
  words = get_words()
  run_bot(words, True)
