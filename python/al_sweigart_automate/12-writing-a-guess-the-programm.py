#!/usr/bin/env python
import random
# Variables (Pyright reportUnboundVariable [E] "..." is possibly unbound)
restartGame = ''
restartMessage = '''
=================== Restart ===================
'''
rangeStart = 1
rangeEnd = 20
print('Hello. What is your name?')
userName = input()

def guessANumber():
    '''Game. Asks user to guess a number'''
    # Variables (Pyright reportUnboundVariable [E] "..." is possibly unbound)
    userGuess = ''
    guessTaken = ''
    secretNumber = random.randint(rangeStart, rangeEnd)

    # actual code
    print(f'Well, {userName}, I am thinking of a number between ' +
          f'{rangeStart} and {rangeEnd}')
    print('Take a guess!')
    for guessTaken in range(1, 7):
        userGuess = input()
        try:
            userGuess = int(userGuess)
            if userGuess > secretNumber:
                print(f'Your guess is to high')
                guessTaken += 1
            elif userGuess < secretNumber:
                print(f'Your guess is to low')
                guessTaken += 1
            else:
                break
        except ValueError:
            if not userGuess:
                print(f'You have not entered anything!')
            else:
                print(f'You have entered "{userGuess}" which is not a number!')
            print('Enter a real number the next time!\n')

    if userGuess == secretNumber:
        print(f'Good job, {userName}! You guessed my number {secretNumber} ' +
              f'in {guessTaken} guesses!')
    else:
        print(f"Nope. The number I was thinking of was {secretNumber}")

    restartGame = input(f"Would you like to have another go? " +
                       f"Type 'yes' to continue or anything else to quit. ")
    try:
        if restartGame == "yes":
            print(restartMessage)
            guessANumber()
    except:
        print(f"You have typed '{restartGame}'. I am quiting!")

guessANumber()

