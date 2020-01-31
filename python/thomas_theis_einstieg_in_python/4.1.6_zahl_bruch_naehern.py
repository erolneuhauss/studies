#!/usr/bin/python

# Modul math
import fractions

x = 1.84953
print "Zahl", x

# als fraction
b3 = fractions.Fraction(x)
print "Fraction:", b3

# approximiert
b4 = b3.limit_denominator(100)
print "Approx auf Nenner max. 100:", b4

# Genauigkeit
wert = 1.0 * b4.numerator / b4.denominator
print "Wert:", wert
print "relativer Fehler:", abs((x - wert)/x)

