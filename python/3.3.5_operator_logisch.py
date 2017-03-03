#!/usr/bin/python

# Zuweisung
x = 12
y = 15
z = 20

# Ausgabe
print "x:", x
print "y:", y
print "z:", z

# Bedingung 1
if x < y and x < z:
	print x, "(x) ist die kleinste Zahl"
if y > x or y > z:
	print y, "(y) ist nicht die kleinste Zahl"
if not y < x:
	print y, "(y) ist nicht kleiner als", x, "(x)"
