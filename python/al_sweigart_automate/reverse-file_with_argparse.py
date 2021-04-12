#!/usr/bin/env python

import argparse, sys

# build the parser
parser = argparse.ArgumentParser(description='Read a file in file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.1')

# parse the arguments
args = parser.parse_args()

print(args)

try:
    f = open(args.filename, 'r')
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
# except:
#     print("A general error occured")
else:
    with f:
# read the file, reverse the contents and print
        lines = f.readlines()
        print(lines)
        lines.reverse()
        print(lines)

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1]) # negative steps used in slice to revert string
finally:
    print(' End of computation '.center(30, '='))
