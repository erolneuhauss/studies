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
print "Bitte rechnen und Ergebnis eingeben"
z = raw_input()

# Umwandlung in ganze Zahl
zahl = int(z)

# Ausgabe
print "Ihre Eingabe:", z

# Mehrfache Verzweigung, logische Operatoren
# Bedingungen mit mehreren Vergleichsoperatoren

if zahl == c:
	print zahl, "ist richtig"
elif zahl < 0 or zahl > 100:
	print zahl, "ist ganz falsch"
elif c-1 <= zahl <= c+1:
	print zahl, "ist ganz nahe dran"
else:
	print zahl, "ist falsch"

#Ende
print "Das Ergebnis:", c
