#!/usr/bin/python
import math

# Funktion, die drei Werte berechnet
def kreis(radius):
    flaeche = math.pi * radius * radius
    umfang = 2 * math.pi * radius
    durchmesser = 2 * radius
    return flaeche, umfang, durchmesser

# 1. Aufruf
f, u, d = kreis(3)
print "Flaeche:", f
print "Umfang:", u
print "Durchmesser:", d

# 2. Aufruf
x = kreis(3)
print "Flaeche:", x[0]
print "Umfang:", x[1]
print "Durchmesser:", x[2]

# Fehler
#ValueError: too many values to unpack
# Die Größe des zurückgelieferten Tupels passt nicht
f, u  = kreis(3)
