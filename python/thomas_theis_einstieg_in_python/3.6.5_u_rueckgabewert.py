#!/usr/bin/python
# Funktion steuer_calc zur Berechnung der Steuer
def steuer_calc(brutto):
    normal_steuer = 18 / 100.0
    luxus_steuer = 22 / 100.0
    if brutto > 2500:
        steuerbetrag = brutto * luxus_steuer
        return steuerbetrag
    else:
        steuerbetrag = brutto * normal_steuer
        return steuerbetrag

# Hauptprogramm 
for brutto in 1800, 2200, 2500, 2900:
    print "Brutto:", brutto, \
    "Steuerbetrag:", steuer_calc(brutto)
