#!/usr/bin/python
def mittelwert(x,y):
    ergebnis = (x + y) / 2.0
#    print "Mittelwert:", ergebnis # wenn hier print-Anweisung, dann unten nicht moeglich
    return ergebnis

# Hauptprogramm
c = mittelwert(3,9)
print "Mittelwert:", c # s.o.

x = 5
print "Mittelwert:", mittelwert(x,4)
