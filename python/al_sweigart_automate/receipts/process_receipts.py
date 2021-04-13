#!/usr/bin/env python
# calculate a subtotal of specified (glob) receipts and move processed files
# into the 'processed' directory
import os,glob,json,shutil

try:
    os.mkdir('./processed')
# FileExistsError exists since python3.3 and is a subclass of much older OSError
# We are using OSError for compatibility reasons
except OSError:
    print(f"'processed' directory already exists. That's fine with us.")

# receipts = glob.glob('new/receipt-[0-7]*.json')
receipts = glob.glob('new/receipt-[0-9]*.json')
# print(receipts)

subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        # print(content)
        subtotal += float(content['value'])
    # "./new/receipt-0.json".split('/') => [ '.', '/new', 'receipt-0.json' ][-1]
    name = path.split('/')[-1]
    destination = f"./processed/{name}"
    shutil.move(path, destination)
    # print(f"moved '{path}' to '{destination}'")

# print to 2 decimal places works only with f-strings in Python 3.6+
print(f"Receipt subtotal: ${subtotal:.2f}")
