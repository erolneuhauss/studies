#!/usr/bin/env python

import argparse, sys

# build the parser
parser = argparse.ArgumentParser(description='Search for words including partial words')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

# parse the arguments
args = parser.parse_args()
snippet = args.snippet.lower()

try:
    with open('/usr/share/dict/words') as f:
        words = f.readlines()
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit
else:

    matches = [word.strip() for word in words if snippet in word.lower()]

    print(matches)
