#!/usr/bin/python

# zwei Listen
fr = ["Paris", "Lyon", "Marseille"]
it = ["Rom", "Pisa"]

# Listen zusammensetzen
stadtliste = fr + it * 2
print stadtliste

# Liste teilweise durchlaufen
for stadt in stadtliste[3:6]:
    print stadt

for stadt in stadtliste:
    print stadt
