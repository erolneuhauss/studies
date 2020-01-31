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

# Schleife initialisieren
zahl = c + 1

# Anzahl initialisieren
versuch = 0

# Schleife mit while
while zahl != c:
# Anzahl Versuche
    versuch = versuch + 1
    print "Bitte rechnen und Ergebnis eingeben"		
    z = raw_input()
    zahl = int(z)

# Verzweigung 

    if zahl == c:
        print zahl, "ist richtig"
    else:
        print zahl, "ist falsch"

# Anzahl ausgeben
print "Das Ergebnis:", c
print "Anzahl Versuche:", versuch
