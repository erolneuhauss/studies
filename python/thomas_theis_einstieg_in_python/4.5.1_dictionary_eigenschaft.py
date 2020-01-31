#!/usr/bin/python

# Erzeugung eines Dictionarys
print """
alter = {"Peter":31, "Julia":28, "Werner":35}
print alter
for personen in alter:
    print personen, alter[personen]
"""
alter = {"Peter":31, "Julia":28, "Werner":35}
print alter
for personen in alter:
    print personen, alter[personen]

# Ersetzen eines Werts
print """
alter["Julia"] = 27
for personen in alter:
    print personen, alter[personen]
"""
alter["Julia"] = 27
for personen in alter:
    print personen, alter[personen]

# Ein Element hinzu
print """
alter["Moritz"] = 22
for personen in alter:
    print personen, alter[personen]
"""
alter["Moritz"] = 22
for personen in alter:
    print personen, alter[personen]

# Ausgabe
print """
print "Julia:", alter["Julia"]
"""
print "Julia:", alter["Julia"]
