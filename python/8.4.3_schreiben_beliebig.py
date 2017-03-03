#!/usr/bin/python3

import sys,os

# Zugriffsversuch
try:
    d = open("obst.txt","r+")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# ich wollte sehen, ob ich die Nummer der Position neben den Bytes
# anzeigen lassen kann - so geht es
#gesamtertext = d.read()
#
#counter = -1
#
#for i in gesamtertext:
#    counter += 1
#    print(counter, i)
# Lesen Einzelpreises
d.seek(67)


d.close()
