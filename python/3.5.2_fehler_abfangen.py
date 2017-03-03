#!/usr/bin/python

# Eingabe
print "Bitte geben Sie eine ganze Zahl ein"		
z = raw_input()

# Versuch der Umwandlung
try:
    zahl = int(z)
    print "Sie haben die ganze Zahl", \
    zahl, "richtig eingegeben"

# Fehler bei der Umwandlung
except:
    print "Sie haben die ganze Zahl nicht richtig eingegeben"

# Ende ausgeben
print "Das Ende des Programms"
