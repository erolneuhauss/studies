#!/usr/bin/python

# Berechnung
a = 23
b = 7.5
c = a + b

# normale Ausgabe

print "Ergebnis: " + str(a) + "+" + str(b) \
    + "=" + str(c)

print

# Liste 
stadt = ["Hamburg", "Berlin", "Augsburg"]
for x in stadt:
    print x

ausgabe = ""
for x in stadt:
    ausgabe += "Stadt" + "=>" + x + " # "
print ausgabe
