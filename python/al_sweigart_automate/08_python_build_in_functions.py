#!/usr/bin/env python

print('\n--- 2. Cell ---')
import pyperclip
pyperclip.copy('Hello')
pyperclip.paste()

print('--- 1. Cell ---')
import sys
print('Hello')
sys.exit()
print('Goodbye')

