#!/usr/bin/env python

def div42by(divideBy):
    try:
        return 42 / divideBy
    except:
        print(f'Error: You tried to divide by {divideBy}.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(4))

keep_asking = True
while keep_asking:
    numCats = input('How many cats do you have? ')
    try:
        numCats = int(numCats)
        if numCats >= 4:
            print('That is a lot of cats!')
        elif numCats == 0:
            print('Alright, you do not have a cat!')
        elif numCats < 0:
            print(f'There is no such thing as to have "{numCats}" cats')
            print('Or are you including cats who have died?')
        else:
            print('That is a not that many cats!')
        keep_asking = False
    except ValueError:
        if not numCats:
            print(f'You have not entered anything!')
        else:
            print(f'You have entered "{numCats}" which is not a number!')
        print('Enter a real number the next time!\n')
