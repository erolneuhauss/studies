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
