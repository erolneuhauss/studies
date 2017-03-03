#!/usr/bin/python

# mehrdimensionale Liste, unterschiedliche Objekte
x = [["Paris", "FR", 3500000],["Rom", "IT", 4200000]]

print x

# Teilliste
print x[0]

print x[0][0], "hat", x[0][2], "Einwohner"
print x[1][0], "hat", x[1][2], "Einwohner"

# Teile von Elementen
print "Laenderkuerzel:", x[0][1][:2]
print "Laenderkuerzel:", x[1][1][:2]
