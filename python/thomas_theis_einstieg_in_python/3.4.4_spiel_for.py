#!/usr/bin/python

# Modul import importieren
import random

# Zufallsgenerator initialisieren
random.seed()

# Zufallswerte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

# Ausgabe
print "Die Aufgabe:", a, "+", b

# Schleife mit for
for i in 1, 2, 3, 4:
    print "Bitte rechnen und Ergebnis eingeben"		
    z = raw_input()
    zahl = int(z)

# Verzweigung 

    if zahl == c:
        print zahl, "ist richtig"
# Abbruch der Schleife
        break
    else:
        print zahl, "ist falsch"

#Ende
print "Das Ergebnis:", c
