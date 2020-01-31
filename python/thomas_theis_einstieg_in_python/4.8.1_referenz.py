#!/usr/bin/python

# Kopie einer Zahl
print "Zahl:"
x = 12.5
y = x
print "Gleiches Objekt:", x is y
y = 15.8
print "Gleiches Objekt:", x is y
print "Gleicher Inhalt:", x == y
print

# Kopie eines Strings
print "String:"
x = "Robinson"
y = x
print "Gleiches Objekt:", x is y
y = "Freitag"
print "Gleiches Objekt:", x is y
print "Gleicher Inhalt:", x == y
print

# Zweite Referenz auf eine Liste
print "Liste:"
x = [23, "hallo", -7.5]
y = x
print "Gleiches Objekt:", x is y
y[1] = "welt"
print "Gleiches Objekt:", x is y
print

