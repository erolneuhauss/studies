#!/usr/bin/python
def sortieren(eins, zwei):
    if eins < zwei:
        return zwei, eins
    else:
        return eins, zwei

# Beispiel 1
x = 24
y = 29
x, y = sortieren(y, x) # die Reihenfolge der Variablen ist bei der Zuweisung fuer die Ausgabe mit print relevant
print "x = ", x, "y =", y # stuende oben y, x, dann muesste unten auch entsprechend print y, x
print sortieren(y, x)

# Beispiel 2
x = 124
y = 29
print "x = ", x, "y =", y # stuende oben y, x, dann muesste unten auch entsprechend print y, x
print sortieren(y, x)

