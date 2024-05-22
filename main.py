import random

hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
               '''
                 +---+
                 |   |
                 O   |
                     |
                     |
                     |
               =========''',
               '''
                 +---+
                 |   |
                 O   |
                 |   |
                     |
                     |
               =========''',
               '''
                 +---+
                 |   |
                 O   |
                /|   |
                     |
                     |
               =========''',
               '''
                 +---+
                 |   |
                 O   |
                /|\  |
                     |
                     |
               =========''',
               '''
                 +---+
                 |   |
                 O   |
                /|\  |
                /    |
                     |
               =========''',
               '''
                 +---+
                 |   |
                 O   |
                /|\  |
                / \  |
                     |
               =========''']

words = (
"egg", "elephant", "eggplant", "apple", "music", "piano", "pasta", "swings", "rabbit", "avocado", "bus", "ship", "cat",
"coat")


def displayBoard(hangmanPics, missedLetters, shownWord):
    print(hangmanPics[len(missedLetters)])
    print("the secret word:")
    print(shownWord)
    print("missed letters:")
    print(missedLetters, sep=" ")


def getGuess(letter, alreadyGuessed):
    if not letter.isalpha():
        return '-1'
    if letter in alreadyGuessed:
        return '-2'
    return letter


def playAgain():
    isToPlay = input("do you want to play again? (enter yes or no)\n")
    isToPlay = isToPlay.lower()
    if (isToPlay == "yes"):
        print("play again")
        return True
    else:
        print("bye-bye")
        isToPlay = input()  # Just so we can see the previous print
        return False


def shown(letter, shownWord):
    for i in range(len(secretWord)):
        if letter == secretWord[i]:
            shownWord = (shownWord[:i] + letter + shownWord[i + 1:])
    return shownWord


gameIsDone = False
missedLetters = ''
correctLetters = ''
secretWord = words[int(random.random() * len(words))]
shownWord = '_' * len(secretWord)
# playMore=False


# The beginning of the game
while not gameIsDone:
    displayBoard(hangmanPics, missedLetters, shownWord)

    guess = input("make a guess\n")
    guess = guess.lower()
    get = getGuess(guess, missedLetters + correctLetters)
    if get == '-1':
        print("invalid input")
    elif get == '-2':
        print("you have already guessed that letter")
    else:  # In case the signal is fine
        shownWord = shown(guess, shownWord)
        if guess in secretWord:  # If the guess is correct
            correctLetters += guess
            print("correct guess")
            if shownWord == secretWord:  # If he finished guessing the whole word
                print('the secret word:\n' + secretWord + '\nYes! you have reached the secret word. you won.')
                if (playAgain()):
                    gameIsDone = False
                    missedLetters = ''
                    correctLetters = ''
                    secretWord = words[int(random.random() * len(words))]
                    shownWord = '_' * len(secretWord)
                else:
                    break
        else:  # If the guess was wrong
            missedLetters += guess
            print("wrong guess")
            if len(missedLetters) == len(hangmanPics) - 1:  # If the guesswork is over
                displayBoard(hangmanPics, missedLetters, shownWord)
                print('Game over!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                    len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True
                if (playAgain()):
                    gameIsDone = False
                    missedLetters = ''
                    correctLetters = ''
                    secretWord = words[int(random.random() * len(words))]
                    shownWord = '_' * len(secretWord)
                else:
                    break