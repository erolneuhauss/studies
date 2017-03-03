#!/usr/bin/python

# Originale
z = "Robinson"
print z, type(z)
t = [4, 12, 6, -2]
print t, type(t)
u = (4, 12, 6, -2)
print u, type(u)

# umgedreht
r = reversed(z)
ausgabe = ""
for x in r:
    ausgabe += x + " "
    print ausgabe
print ausgabe

# Sortierte Listen
s1 = sorted(z)
ausgabe = ""
for x in s1:
    ausgabe += x + " "
print ausgabe

s2 = sorted(t)
print s2
for x in s2:
    print x
#ausgabe = ""
#for x in s2:
#    ausgabe += x + ""
#print ausgabe
