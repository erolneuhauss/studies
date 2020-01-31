#!/usr/bin/python

# Programm zur Berechnung des monatlich zu zahlenden Steuerbetrags

steuer = 18 / 100.0

luxus_steuer = 22 / 100.0

print "Bitte geben Sie Ihr Bruttogehalt in Euro ein:"

brutto = raw_input()

# Umwandeln in eine ganze Zahl
brutto_integer = int(brutto)

# Berechnung 

if brutto_integer > 2500:
	steuerbetrag = brutto_integer * luxus_steuer
	print "Ihre Eingabe:", brutto_integer 
	print "Es ergibt sich aufgrund des Luxus-", \
	"steuersatzes", luxus_steuer, "Ein Steuer-", \
	"betrag von", steuerbetrag, "EURO"
	
else:
	steuerbetrag = brutto_integer * steuer
	print "Ihre Eingabe:", brutto_integer 
	print "Es ergibt sich aufgrund des Normal-", \
	"steuersatzes", steuer, "Ein Steuer-", \
	"betrag von", steuerbetrag, "EURO"
