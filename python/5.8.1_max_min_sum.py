#!/usr/bin/python
t1 = (3, 12, 9)
print "t1", t1
print "Max:", max(t1)
print "Min:", min(t1)
print "Summe:", sum(t1)

t2 = (1, 0, 13, 1, 2)
print "t2", t2
print "Summe:", sum(t2)
# max(t1, t2) berechnet die Summe von t1 und vergleicht die Summe von t2 und gibt den Tupel mit der höchsten Summe aus
print "Max Summe:", max(t1, t2)
print "Min Summe:", min(t1, t2)
# TypeError: can only concatenate tuple (not "int") to tuple
print "Summe:", sum(t1,t2)
# TypeError: 'int' object is not iterable
print "Summe:", sum(sum(t1), sum(t2))
