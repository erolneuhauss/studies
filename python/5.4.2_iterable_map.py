#!/usr/bin/python

# Funktion mit einem Parameter
def quad(x):
    erg = x * x
    return erg

# Funktion mit mehr als einem Parameter
def summe(a, b, c):
    erg = a + b + c
    return erg

# Funktion mit einem Parameter mehrmals aufrufen
x = [4, 2.5, -1.5]
z = map(quad,x)

for i in x:
    print i, "*", i

# Jedes Ergebnis ausgeben
print "Quadrat:"
for element in z:
    print element
print

# Funktion mit mehr als einem Parameter mehrmals aufrufen
a = [3, 1.2, 2] 
b = [4.8, 2, 5]
c = [5, 0.1, 9]

for i in a, b, c:
    print i

z = map(summe, a, b, c)

# Jedes Ergebnis ausgeben
print "Summe:"
for element in z:
    print element
print

