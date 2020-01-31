#!/usr/bin/python

# Programm zur Berechnung des monatlich zu zahlenden Steuerbetrags

steuer = 18 / 100.0

print "Bitte geben Sie Ihr Bruttogehalt in Euro ein:"

brutto = raw_input()

# Umwandeln in eine ganze Zahl
brutto_integer = int(brutto)

# Berechnung 
steuerbetrag = brutto_integer * steuer


# Ausgabe
print "Ihre Eingabe:", brutto_integer 

print "Steuersatz:", steuer

print "Es ergibt sich ein Steuerbetrag von:", steuerbetrag , "EURO"
