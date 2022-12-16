from bot import Bot


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def test_check(bot, guess, pattern, word, expected):
  if bot.check(guess, pattern, word) != expected:
    print(bcolors.FAIL +
          f"FAILED:{guess=},{pattern=},{word=},{expected=}"+bcolors.ENDC)
    return False
  return True


def test_check_move(bot, letter, index, word, expected):
  if bot.check_move(letter, index, word) != expected:
    print(bcolors.FAIL +
          f"FAILED:{letter=},{index=},{word=},{expected=}"+bcolors.ENDC)
    return False
  return True


def test_check_move_all(bot):
  print("\n"+bcolors.OKCYAN+bcolors.BOLD+"Testing check_move"+bcolors.ENDC)
  tests = [
      # second t ok, checked elsewhere
      test_check_move(bot, "l", 1, "close", False),
      test_check_move(bot, "t", 4, "stent", True),
      test_check_move(bot, "c", 0, "close", False)
  ]
  print(bcolors.OKGREEN+f"correct:{sum(tests)}"+bcolors.ENDC)
  print(bcolors.FAIL+f"failed:{len(tests)-sum(tests)}"+bcolors.ENDC)


def test_check_all(bot):
  print("\n"+bcolors.OKCYAN+bcolors.BOLD+"Testing check_move"+bcolors.ENDC)
  tests = [
      # check placement for empty
      test_check(bot, "irate", "_____", "ioooo", False),
      test_check(bot, "irate", "_____", "orooo", False),
      test_check(bot, "irate", "_____", "ooaoo", False),
      test_check(bot, "irate", "_____", "oooto", False),
      test_check(bot, "irate", "_____", "ooooe", False),
      test_check(bot, "irate", "_____", "ooooo", True),

      # check fail for move:
      test_check(bot, "irate", "ooooo", "ioooo", False),
      test_check(bot, "irate", "ooooo", "orooo", False),
      test_check(bot, "irate", "ooooo", "ooaoo", False),
      test_check(bot, "irate", "ooooo", "oooto", False),
      test_check(bot, "irate", "ooooo", "ooooe", False),
      test_check(bot, "irate", "ooooo", "ooooo", False),

      # check placement for move
      test_check(bot, "irate", "o____", "ioooo", False),
      test_check(bot, "irate", "_o___", "orooo", False),
      test_check(bot, "irate", "__o__", "ooaoo", False),
      test_check(bot, "irate", "___o_", "oooto", False),
      test_check(bot, "irate", "____o", "ooooe", False),
      test_check(bot, "irate", "o____", "iiooo", False),
      test_check(bot, "irate", "_o___", "orroo", False),
      test_check(bot, "irate", "__o__", "ooaao", False),
      test_check(bot, "irate", "___o_", "ooott", False),
      test_check(bot, "irate", "____o", "oooee", False),
      test_check(bot, "irate", "o____", "oiooo", True),
      test_check(bot, "irate", "_o___", "ooroo", True),
      test_check(bot, "irate", "__o__", "oooao", True),
      test_check(bot, "irate", "___o_", "oooot", True),
      test_check(bot, "irate", "____o", "oooeo", True),

      # check exact
      test_check(bot, "irate", "xxxxx", "ioooo", False),
      test_check(bot, "irate", "xxxxx", "orooo", False),
      test_check(bot, "irate", "xxxxx", "ooaoo", False),
      test_check(bot, "irate", "xxxxx", "oooto", False),
      test_check(bot, "irate", "xxxxx", "ooooe", False),
      test_check(bot, "irate", "xxxxx", "ooooo", False),

      # check placement for exact:
      test_check(bot, "irate", "x____", "ioooo",	True),
      test_check(bot, "irate", "_x___", "orooo",	True),
      test_check(bot, "irate", "__x__", "ooaoo",	True),
      test_check(bot, "irate", "___x_", "oooto",	True),
      test_check(bot, "irate", "____x", "ooooe",	True),

      # check doubles (zero correct)

      # check doubles (one correct)

      # random tests:
      test_check(bot, "irate", "__xxx", "crate", False),
      test_check(bot, "irate", "__xxx", "elate", True),
      test_check(bot, "irate", "xx_x_", "irote", False),
      test_check(bot, "irate", "xx_x_", "irats", False),
      test_check(bot, "irate", "xx_x_", "irots", True)
  ]
  print(bcolors.OKGREEN+f"correct:{sum(tests)}"+bcolors.ENDC)
  print(bcolors.FAIL+f"failed:{len(tests)-sum(tests)}"+bcolors.ENDC)


if __name__ == "__main__":
  test_bot = Bot("valid-wordle-words.txt")
  test_check_move_all(test_bot)
  test_check_all(test_bot)
