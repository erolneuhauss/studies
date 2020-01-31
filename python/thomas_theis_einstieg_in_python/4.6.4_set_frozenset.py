#!/usr/bin/python

# Set
s1 = set([8, 15, "x", 8])

print "set 1:", s1

# frozenset
fs = frozenset([8, 15, "x", 8])

print "frozenset 1:", fs

for x in fs:
    print x
fs.discard("x")
