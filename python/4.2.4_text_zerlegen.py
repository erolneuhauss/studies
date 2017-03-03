#!/usr/bin/python

# Beispiel
test = "Das ist ein Beispielsatz"
print "Text:", test

# Beginn, Ende
if test.startswith("Das"):
    treffer = test.startswith("Das") # Rueckgabewert true|false
    print "Text beginnt mit Das:", treffer
if not test.endswith("Das"):
    treffer = test.endswith("Das") # Rueckgabewert true|false
    print "Text endet nicht mit Das:", treffer

# Zerlegung
teile = test.partition("ei")
print "vor der 1. Teilung:", teile[0]
print "hinter der 1. Teilung:", teile[2]

teile = test.rpartition("ei")
print "vor der 2. Teilung:", teile[0]
print "hinter der 2. Teilung:", teile[2]

# Zerlegung in Liste
wliste = test.split()
for i in range(0,4):
    print "Element:", i, wliste[i]
