from game import Game
from sys import argv

if __name__ == "__main__":
  wordle = Game("valid-wordle-words.txt", 6)
  if len(argv) == 1:
    wordle.run(True)
  else:
    game = wordle.test_game()
    if len(game) <= 6:
      print("won game")
    else:
      print("lost game")
