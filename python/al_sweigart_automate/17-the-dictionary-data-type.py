#!/usr/bin/env python
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
#message = 'hello'
count = {} # 'l': 2

for char in message:
#    print(char)
    count.setdefault(char, 0)
    count[char] = count[char] + 1

print(count)
pprint.pprint(count)

count = {} # 'l': 2

for char in message.upper():
#    print(char)
    count.setdefault(char, 0)
    count[char] = count[char] + 1

print(count)
pprint.pprint(count)

stored_here = pprint.pformat(count)
print(stored_here)
