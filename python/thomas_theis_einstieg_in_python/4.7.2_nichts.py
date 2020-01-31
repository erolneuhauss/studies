#!/usr/bin/python

# Funktion
def quotient(a, b):
    try:
        c = a / b 
        return c
    except:
        print "Funktion meldet Fehler"

# liefert Ergebnis
erg = quotient(7.0,4)
if erg:
    print "Ergebnis liefert Ergebnis:", erg
    print "Wahrheitswert:", bool(erg)
    print "Type:", type(erg)
else:
    print "Ergebnis liefert Fehler:", erg, bool(erg)
    print "Wahrheitswert:", bool(erg)
    print "Type:", type(erg)

erg = quotient(7,0)
if erg:
    print "Ergebnis liefert Ergebnis:", erg
    print "Wahrheitswert:", bool(erg)
    print "Type:", type(erg)
else:
    print "Ergebnis liefert Fehler:", erg
    print "Wahrheitswert:", bool(erg)
    print "Type:", type(erg)

# Konstante None
z = None
print "Konstante None:", z
if z is None:
    print "Objekt ist:", z
    print "Wahrheitswert:", bool(z)
    print "Type:", type(z)
else:
    print "Objekt ist:", z, bool(z)
    print "Wahrheitswert:", bool(z)
    print "Type:", type(z)
