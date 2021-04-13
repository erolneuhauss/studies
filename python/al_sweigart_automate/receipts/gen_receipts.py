#!/usr/bin/env python
# generate a dictionary entry like: {"topic": "seraphs", "value": "535.61"}
# in ./new directory like: receipt-9.json
import random,json,os

try:
    os.mkdir('./new')
# FileExistsError exists since python3.3 and is a subclass of much older OSError
# We are using OSError for compatibility reasons
except OSError:
    print(f"'processed' directory already exists. That's fine with us.")

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
            'topic': random.choice(words),
            'value': '{:.2f}'.format(amount)
            }
    with open(f'./new/receipt-{identifier}.json', 'w') as f:
        json.dump(content, f)
