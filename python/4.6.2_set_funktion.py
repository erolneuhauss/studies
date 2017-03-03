#!/usr/bin/python

# Set
s1 = set([8, 15, "x"])
print "Original:", s1
for i in s1:
    print i

# Kopie
s2 = s1.copy()
print "Kopie:", s2
for i in s2:
    print i

# Element hinzu
s1.add("abc")
print "Element hinzu:", s1
for i in s1:
    print i

# Element entnehmen
s1.discard("x")
print "Element entnommen:", s1
for i in s1:
    print i

# Leeren
s1.clear()
print "geleert:", s1
for i in s1:
    print i

