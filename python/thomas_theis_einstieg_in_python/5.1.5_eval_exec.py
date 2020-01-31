#!/usr/bin/python
import math

# Zwei Fkts
def mw1(a,b):
    c = (a + b) / 2.0
    return c

def mw2(a,b):
    c = (a * b)
#    c = math.sqrt(a * b) # schwer verstaendliches Beispiel!
    return c

def mw3(a,b):
    c = a ** b
    return c

# eval ist in der Lage, Python-Code zusammenzusetzen
# hier werden drei Werte in c zwischengespeichert
# c = mw1(3,4), c = mw2(3,4), c = mw3(3,4) 
# anders ausgedrueckt: drei Ausdruecke in Zeichenketten zusammensetzen
# ermittelt den Wert des Ausdrucks
for i in range(1,4):
    t = "mw" + str(i) + "(3, 4)"
    c = eval(t)    
    print c
print

# exec fuehrt eine zusammengesetzte Anweisung aus
# drei Anweisungen in Zeichenketten zusammengesetzt:
# print "mw1(3,4)" print "mw2(3,4)" print "mw3(3,4)"
# der Rueckgabewert wird direkt ausgegeben
for i in range(1,4):
    t = "print mw" + str(i) + "(3, 4)"
    exec t
