#!/usr/bin/python
import u_modul_finanz
# Hauptprogramm 

for brutto in 1800, 2200, 2500, 2900:
    print "Brutto:", brutto, \
    "Steuerbetrag:", u_modul_finanz.steuer_calc(brutto)
