#!/usr/bin/python

# Set
s1 = set([8, 15, "x"])
s2 = set([4, "x", "abc", 15])

print "set 1:", s1

print "set 2:", s2

s3 = s1 | s2
print "Vereinigungsmenge:", s3

s4 = s1 & s2
print "Schnittmenge:", s4

s5 = s1 - s2
print "Differenzmenge s1-s2:", s5

s6 = s2 - s1
print "Differenzmenge s2-s1:", s6

s7 = s1 ^ s2
print "symm. Differenzmenge:", s7



