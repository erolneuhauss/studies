#!/usr/bin/env python

import random

def guessANumber():
    print('Hello. What is your name?')
    userName = input()
    rangeStart = 1
    rangeEnd = 21
    print(f'Well, {userName}, I am thinking of a number between ' +
          f'{rangeStart} and {rangeEnd}')
    print('Take a guess!')

    randomNum = random.randint(rangeStart, rangeEnd)
    numberOfTries = 0
    while numberOfTries <=7:
        userGuess = input()
        try:
            userGuess = int(userGuess)
            if numberOfTries == 7:
                print(f'Nope. The number I was thinking was {randomNum}')
                break
            if userGuess > randomNum:
                print(f'Your guess is to high')
                numberOfTries += 1
            elif userGuess < randomNum:
                print(f'Your guess is to low')
                numberOfTries += 1
            else:
                print(f'Good job, {userName}! ' +
                      f'You guessed my number {randomNum} ' +
                      f'in {numberOfTries} guesses!')
                break
        except ValueError:
            if not userGuess:
                print(f'You have not entered anything!')
            else:
                print(f'You have entered "{userGuess}" which is not a number!')
            print('Enter a real number the next time!\n')

    restartMessage = '''
    =================== Restart ===================
    '''
    keep_going = input(f"Would you like to have another go? " +
                       f"Type 'yes' to continue or anything else to quit. ")
    try:
        if keep_going == "yes":
            print(restartMessage)
            guessANumber()
    except:
        print(f"You have typed '{keep_going}'. I am quiting!")

guessANumber()

