#!/usr/bin/env python

print('--- 1. Cell ---')
spam = 42 # global variable
def eggs():
    spam = 42 # local variable

print(eggs())

print('\n--- 2. Cell ---')
def spam():
    eggs = 42 # local variable
    bacon()
    return eggs

def bacon():
    eggs = 0    # same as the above local variable,
                # but in actuality it is another local variable
    return eggs

print(spam())

print('\n--- 3. Cell ---')
print(bacon())

print('\n--- 4. Cell ---')
def mySpam():
    return eggs

eggs = 100
print(mySpam())

print('\n--- 5. Cell ---')
def myEggs():
    eggs = 99
    return eggs

eggs = 100
myEggs()
print(eggs)     # global variable does NOT get overwritten by myEggs()!
print(myEggs()) # local variable does NOT get overwritten by global variable

print('\n--- 6. Cell ---')
def myEggs():
    global eggs # treat as a global variable
    eggs = 99
    return eggs

eggs = 100      # therefore this variable gets overwritten by myEggs()
myEggs()
print(eggs)
