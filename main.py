from bot import Bot

if __name__ == "__main__":
  wordle_bot = Bot("valid-wordle-words.txt", True)
  wordle_bot.run()
