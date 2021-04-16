#!/usr/bin/env python
import re
message = 'Call me 415-555-1234 tomorrow, or at 415-555-9999 for my office'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me 415-555-1234 tomorrow, or at 415-555-9999 for my office')
print(mo.group())
