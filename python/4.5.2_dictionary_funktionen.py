#!/usr/bin/python

# Erzeugung eines Dictionarys
alter = {"Peter":31, "Julia":28, "Werner":35}
for personen in alter:
    print personen, alter[personen]
print ""

# Elemente enthalten?
if "Julia" in alter:
    print "Julia:", alter["Julia"]
print ""

# Entfernen eines Elements
del alter["Julia"]
for personen in alter:
    print personen, alter[personen]
print ""

# Element Julia enthalten?
if "Julia" not in alter:
    print "Julia ist nicht enthalten"
print ""

# Anzahl Elemente
print "Anzahl:", len(alter)
print ""

# Aktualisierung mit zweitem Dictionary
ualter = {"Moritz": 18, "Werner": 29}
alter.update(ualter)
for personen in alter:
    print personen, alter[personen]
print ""
