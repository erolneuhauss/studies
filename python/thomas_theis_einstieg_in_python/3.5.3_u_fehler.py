#!/usr/bin/python

inch = 2.54

# Schleife initialisieren
versuch = 0

# Schleife mit while
while versuch == 0:
    try:
        print "Bitte einen inch-Wert eingeben," \
        "den ich in cm umwandle"		
        z = raw_input()
        zahl = int(z)
        print zahl, "inch =", zahl * inch, "cm"
        versuch = 1
# Anzahl Versuche
    except:
        print "Sie haben die ganze Zahl nicht richtig eingegeben"

print "Das Ende des Programms"
