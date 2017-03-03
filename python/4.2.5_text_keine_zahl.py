#!/usr/bin/python

# Erste Zeichenkette
x = "15.3p"

try:
    x = float(x)
    ergebnis = x * 2
    print ergebnis
except:
    print "Zeichenkette konnte nicht umgewandelt werden"
