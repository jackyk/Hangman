import random
#global vars when starting the game
listOfWords = ["example", "says", "python", "rocks"]
guessWord = random.choice(listOfWords)
board = [" * " for char in guessWord]
alreadySaid = ""


        global guessWord, board, alreadySaid
        whatplayersaid = raw_input("Guess a letter: ")
        if whatplayersaid in guessWord:
          board = [char if char == whatplayersaid or char in alreadySaid else " * " for char in guessWord]
          board = "".join(board)
          print(board)
        else:
         print("Nope")
        alreadySaid = alreadySaid + whatplayersaid
        # Hangman.Playing()
