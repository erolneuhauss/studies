#!/usr/bin/env python

print('--- 1. Cell ---')
spam = 0
while spam < 5:
    print('Hello world!')
    spam = spam + 1

print('\n--- 2. Cell ---')
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you')

print('\n--- 3. Cell ---')
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you')

print('\n--- 4. Cell ---')
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

