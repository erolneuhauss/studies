#!/usr/bin/python

# true and false
w = True
print w
w = False
print w
w = 5 > 3
print w
w = 5 < 3
print w
print

# Datentyp
w = 5 > 3
print type(w)

# wahre Zahl
z = 5 + 0.001 - 5
print z
if z:
    print bool(z)
print

# nicht wahre Zahl
z = 5.75 - 5.75
print "z = 5.75 - 5.75=", z
if not z: # wenn die Variable z nichts enthaelt (if not)
    print bool(z)
print

# String
s = "Kurt"
print s
if s:
    print bool(s)
else:
    print bool(s)

# String
s = ""
print "s = ''", s
if not s: # wenn die Variable s nichts enthaelt (if not)
    print bool(s)

# Liste 
l = [3, 4]
print "liste vorher:", l
if not l:
    print "liste ist leer, also:", bool(l)
else:
    print "liste ist nicht leer, also:", bool(l)
del l[0:2]
print "liste nachher:", l
if not l:
    print "liste ist leer, also:", bool(l)
else:
    print "liste ist nicht leer, also:", bool(l)

# Tupel
t = (5, 8, 2)
print "Tupel:", t
if not t:
    print "Tupel ist leer, also:", bool(t)
else:
    print "Tupel ist nicht leer, also:", bool(t)

# Dictionary
d = {"Julia":28, "Werner":35}
print "Dictionary vorher:", d
if not d:
    print "Dictionary ist leer, also:", bool(d)
else:
    print "Dictionary ist nicht leer, also:", bool(d)
del d["Julia"]
del d["Werner"]
if not d:
    print "Dictionary ist leer, also:", bool(d)
else:
    print "Dictionary ist nicht leer, also:", bool(d)

# Set
s = set([5, 7.5, "abc"])
print "set vorher:", s
if not s:
    print "Set ist leer, also:", bool(s)
else:
    print "Set ist nicht leer, also:", bool(s)
s.clear()
print "set nachher:", s
if not s:
    print "Set ist leer, also:", bool(s)
else:
    print "Set ist nicht leer, also:", bool(s)
