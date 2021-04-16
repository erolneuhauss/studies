#!/usr/bin/env python
import re
message = 'Call me 415-555-1234 tomorrow, or at 415-555-9999 for my office'

print(' 1. Cell '.center(30, '-'))
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me 415-555-1234 tomorrow, or at 415-555-9999 for my office')
print(mo.group())

print(' 2. Cell '.center(30, '-'))
mo = phoneNumRegex.findall('Call me 415-555-1234 tomorrow, or at 415-555-9999 for my office')
print(mo)

print(' 3. Cell '.center(30, '-'))
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
mo = vowelRegex.findall('Robocop Eats Baby Food')
print(mo)
