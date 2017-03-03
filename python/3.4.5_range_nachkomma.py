#!/usr/bin/python

# Ausgabe einer for-schleife mit range

# 1. Version
for i in range(18,22):
	print "Zahl:", i, "Ein zehntel:", i/10.0
print "Ende"

# 2. Version
x = 1.8
for i in range(4):
    print "Zahl:", x
    x = x + 0.1
print "Ende"
