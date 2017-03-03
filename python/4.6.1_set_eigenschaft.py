#!/usr/bin/python

# liste
li = [8, 2, 5, 5, 5]
print li
for i in li:
    print i

# Set
s1 = set([8, 2, 5, 5, 5])
print "Set:", s1
for i in s1:
    print i

v = 5

if v in s1:
    print v, "ist enthalten"

print "Anzahl:", len(s1)
