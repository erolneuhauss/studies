#!/usr/bin/python
# Funktion steuer_calc zur Berechnung der Steuer
def steuer_calc(brutto):
    normal_steuer = 18 / 100.0
    luxus_steuer = 22 / 100.0
    if brutto > 2500:
        steuerbetrag = brutto * luxus_steuer
        print "Brutto:", brutto, "Luxussteuer", luxus_steuer, \
        "Steuerbetrag:", steuerbetrag
    else:
        steuerbetrag = brutto * normal_steuer
        print "Brutto:", brutto, "Normalsteuer:", normal_steuer, \
        "Steuerbetrag:", steuerbetrag

# Hauptprogramm 
steuer_calc(1800)
steuer_calc(2200)
steuer_calc(2500)
steuer_calc(2900)
