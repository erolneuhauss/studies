#!/usr/bin/python

import copy

# Kopie einer Liste, Methode 1
x = [23, "hallo", -7.5]
y = []
for i in x:
    y.append(i)
print "x:", x, "y:", y, "gleiches Objekt?", x is y
print "x:", x, "y:", y, "gleicher Inhalt?", x == y

# Kopie einer Liste, Methode 2
x = [23, ["Berlin", "Hamburg"], -7.5, 12, 67]
y = copy.deepcopy(x) # Funktion zur Tiefenkopie
print "x:", x, "y:", y, "gleiches Objekt?", x is y
print "x:", x, "y:", y, "gleicher Inhalt?", x == y
