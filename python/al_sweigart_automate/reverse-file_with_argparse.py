#!/usr/bin/env python

import argparse

# build the parser
parser = argparse.ArgumentParser(description='Read a file in file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.1')

# parse the arguments
args = parser.parse_args()

print(args)

# read the file, reverse the contents and print
with open(args.filename, 'r') as f:
    lines = f.readlines()
    print(lines)
    lines.reverse()
    print(lines)

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip()[::-1])
