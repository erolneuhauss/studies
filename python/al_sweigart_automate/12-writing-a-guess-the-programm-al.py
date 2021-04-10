#!/usr/bin/env
import random
print('Hello! What is your name?')
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print(f"Your guess is to low.")
    elif guess > secretNumber:
        print(f"Your guess is to high.")
    else:
        break   # This condition is for the correct guess!

if guess == secretNumber:
    print(f"Good job, {name}! You guessed my number in {guessTaken} guesses.")
else:
    print(f"Nope. The number I was thinking of was {secretNumber}")
