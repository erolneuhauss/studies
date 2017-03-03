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

# Eingabe einer Zahl des Users
print "Bitte eine ganze Zahl eingeben"
z = raw_input()

# Umwandlung in ganze Zahl
zahl = int(z)

# Ausgabe
print "Ihre Eingabe:", z

print "Das Ergebnis:", c
