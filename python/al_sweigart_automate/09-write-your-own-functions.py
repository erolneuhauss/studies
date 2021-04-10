#!/usr/bin/env python

print('--- 1. Cell ---')
def hello():
    print('Hello!')
    print('Howdy!!!')
    print('Hello there!!')

hello()
hello()
hello()

print('\n--- 2. Cell ---')
def addedHello(name):
    print('Hello ' + name)
    addMessage = name + ' has ' + str(len(name)) + ' letters in it.'
    print(addMessage)

addedHello('Alice')
addedHello('Bob')

print('\n--- 3. Cell ---')
def plusOne(number):
    return number + 1

plusOne(5)
newNumber = plusOne(5)
print(newNumber)

print('\n--- 4. Cell ---')
print(plusOne(7))
