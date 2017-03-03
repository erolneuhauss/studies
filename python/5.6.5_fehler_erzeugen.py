#!/usr/bin/python

fehler = True
while fehler:
    try:
        zahl = float(raw_input("Eine positive Zahl: "))
        if zahl < 0:
            raise
        kw = 1.0 / zahl
        fehler = False
    except:
        print "Fehler"

# Ausgabe
print "Der Kehrwert von", zahl, "ist", kw
