#!/usr/bin/python

inch = 2.54

# Schleife initialisieren
zahl = 1

# Anzahl initialisieren
versuch = 0

# Schleife mit while
while zahl != 0:
    print "Bitte inches eingeben, die ich in cm umwandle"		
    print "(0 eingeben um das Programm zu beenden)"		
    z = raw_input()
    zahl = int(z)
    if zahl == 0:
        break
    else:
# Anzahl Versuche
        versuch = versuch + 1
        print zahl, "inch =", zahl * inch, "cm"

print "Anzahl Versuche:", versuch
