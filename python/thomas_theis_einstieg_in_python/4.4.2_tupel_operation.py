#!/usr/bin/python

# Tupel mit und ohne Klammer
z = (3, 6, -8, 5.5)
print "Tupel 1:", z

z = 6, 8, -3
print "Tupel 2:", z

# mehrdimensionales Tupel, unterschiedliche Objekte
x = (("Paris", "FR", 3500000),["Rom", "IT", 4200000])
print "mehrdim. Tupel"
print x

# Ersetzen
print "Versuche Paris durch Lyon zu ersetzen"
try:
    x[0][0] = "Lyon"
    print "Paris durch Lyon ersetzt"
except:
    print "Fehler: TypeError: 'tuple' object does not support item assignment. Ein Tupel kann nicht veraendert werden"

print "Versuche Rom durch Pisa zu ersetzen"
try:
    x[1][0] = "Pisa"
    print "Listenelement erstetzt:", x[1]
except:
    print "unbekannter Fehler"

# Tupel bei for-Schleife
for i in 4, 5, 12:
    print "i:", i

# Zuweisung mit Tupel
x, y = 2, 18
print "x:", x, "y:", y
