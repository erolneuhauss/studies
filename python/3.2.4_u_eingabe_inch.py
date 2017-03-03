#!/usr/bin/python

# Programm zum Umwandeln von inches in zentimeter
# 1 inch sind 2.54 cm
inch = 2.54

print "Bitte geben Sie einen Inch-Wert ein, den ich in Zentimeter umwandle"

inch_input = raw_input()

# Umwandeln in eine ganze Zahl
inch_input_integer = int(inch_input)

# Berechnung 
cm = inch * inch_input_integer


# Ausgabe
print "Ihre Eingabe:", inch_input_integer 

print "Das Ergebnis:", inch_input_integer , "inch sind", cm, "cm"
