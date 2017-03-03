#!/usr/bin/python

# Initialisierung der while-Schleife
fehler = 1

# Schleife bei falscher Eingabe
while fehler == 1:
# Eingabe
    print "Bitte geben Sie eine ganze Zahl ein"		
    z = raw_input()

# Versuch der Umwandlung
    try:
        zahl = int(z)
        print "Sie haben die ganze Zahl", \
        zahl, "richtig eingegeben"
        fehler = 0

# Fehler bei der Umwandlung
    except:
        print "Sie haben die ganze Zahl nicht richtig eingegeben"

# Ende ausgeben
print "Das Ende des Programms"
