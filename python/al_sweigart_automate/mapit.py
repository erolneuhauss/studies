#!/usr/bin/env python
"""Open given Address with the default webbrowser"""
import sys
import webbrowser

import pyperclip

if len(sys.argv) > 1:  # ['mapit.py', 'Köln', 'Bonn', 'Flughafen']
    # -> Köln Bonn Flughafen.
    ADDRESS = " ".join(sys.argv[1:])
else:
    ADDRESS = pyperclip.paste()

# https://www.google.de/maps/place/K%C3%B6ln+Bonn+Airport/@50.8679152,7.0949077,14.04z/data=!4m5!3m4!1s0x47beded752e8c6ef:0x64972536cb454bc8!8m2!3d50.8666228!4d7.1412431
# https://www.google.de/maps/place/<ADDRESS>
webbrowser.open(f"https://www.google.de/maps/place/{ADDRESS}")
