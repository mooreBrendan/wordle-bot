from bot import Bot
from game import Game


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


def test_check(bot, prev_guess, pattern, new_guess, expected):
  if bot.check(prev_guess, pattern, new_guess) != expected:
    print(bcolors.FAIL +
          f"FAILED:{prev_guess=},{pattern=},{new_guess=},{expected=}"+bcolors.ENDC)
    return False
  return True


def test_check_move(bot, letter, index, prev_guess, expected):
  if bot.check_move(letter, index, prev_guess) != expected:
    print(bcolors.FAIL +
          f"FAILED:{letter=},{index=},{prev_guess=},{expected=}"+bcolors.ENDC)
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
  print("\n"+bcolors.OKCYAN+bcolors.BOLD+"Testing check"+bcolors.ENDC)
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
      test_check(bot, "keeps", "_o___", "abbey", True),
      test_check(bot, "algae", "x___o", "abbey", True),
      test_check(bot, "orbit", "__x__", "abbey", True),
      test_check(bot, "abate", "xx__o", "abbey", True),
      test_check(bot, "opens", "__o__", "abbey", True),
      test_check(bot, "babes", "ooxx_", "abbey", True),
      test_check(bot, "kebab", "_oxoo", "abbey", True),
      test_check(bot, "abyss", "xxo__", "abbey", True),
      test_check(bot, "annal", "o_xxx", "banal", True),
      test_check(bot, "union", "_o___", "banal", True),
      test_check(bot, "alloy", "oo___", "banal", True),
      test_check(bot, "aahed", "o____", "alton", False),
      test_check(bot, "aahed", "o____", "basty", True),
      test_check(bot, "aahed", "o____", "baals", False),

      # check doubles (one correct)

      # check triples
      test_check(bot, "aaabb", "oo___", "ccaaa", False),
      test_check(bot, "aaabb", "oo___", "cccaa", True),
      test_check(bot, "aabbb", "oo___", "ccaaa", True),
      test_check(bot, "aabbb", "oo___", "cccaa", True),
      test_check(bot, "aabbb", "oo___", "cccca", False),
      test_check(bot, "aabbb", "o____", "ccaaa", False),
      test_check(bot, "aabbb", "o____", "cccaa", False),
      test_check(bot, "aabbb", "o____", "cccca", True),

      # random tests:
      test_check(bot, "irate", "__xxx", "crate", False),
      test_check(bot, "irate", "__xxx", "elate", True),
      test_check(bot, "irate", "xx_x_", "irote", False),
      test_check(bot, "irate", "xx_x_", "irats", False),
      test_check(bot, "irate", "xx_x_", "irots", True),
  ]
  print(bcolors.OKGREEN+f"correct:{sum(tests)}"+bcolors.ENDC)
  print(bcolors.FAIL+f"failed:{len(tests)-sum(tests)}"+bcolors.ENDC)


def test_game_eval(test_game, guess, answer, expected_pattern):
  pattern = test_game.evaluate(guess, answer)
  if pattern != expected_pattern:
    print(bcolors.FAIL +
          f"FAILED:{guess=},{answer=},{pattern=},{expected_pattern=}"+bcolors.ENDC)
    return False
  return True


def test_game_eval_all(test_game):
  print("\n"+bcolors.OKCYAN+bcolors.BOLD+"Testing game eval"+bcolors.ENDC)
  tests = [
      test_game_eval(test_game, "irate", "bcdfg", "_____"),
      test_game_eval(test_game, "irate", "eirat", "ooooo"),
      test_game_eval(test_game, "irate", "apple", "__o_x"),
      test_game_eval(test_game, "irate", "irate", "xxxxx"),
      test_game_eval(test_game, "irate", "crate", "_xxxx"),
      test_game_eval(test_game, "irate", "blate", "__xxx"),
      test_game_eval(test_game, "irate", "orote", "_x_xx"),

      # double
      test_game_eval(test_game, "ranee", "range", "xxx_x"),
      test_game_eval(test_game, "pools", "apple", "o__x_"),
      test_game_eval(test_game, "apple", "pools", "_o_x_"),
  ]
  print(bcolors.OKGREEN+f"correct:{sum(tests)}"+bcolors.ENDC)
  print(bcolors.FAIL+f"failed:{len(tests)-sum(tests)}"+bcolors.ENDC)


def test_game_bunch(test_game, count):
  print("\n"+bcolors.OKCYAN+bcolors.BOLD+"Testing game bunch"+bcolors.ENDC)
  fails = 0
  for _ in range(count):
    if _ % 10 == 0:
      print(_)
    rounds = test_game.test_game()
    if len(rounds) > test_game.num_guesses:
      fails += 1
      print(bcolors.FAIL + f"FAILED:{rounds=}"+bcolors.ENDC)

  print(bcolors.OKGREEN+f"correct:{count-fails}"+bcolors.ENDC)
  print(bcolors.FAIL+f"failed:{fails}"+bcolors.ENDC)


if __name__ == "__main__":
  test_bot = Bot("valid-wordle-words.txt")
  test_game = Game("valid-wordle-words.txt", 6)
  test_check_move_all(test_bot)
  test_check_all(test_bot)
  test_game_eval_all(test_game)
  test_game_bunch(test_game, 500)
