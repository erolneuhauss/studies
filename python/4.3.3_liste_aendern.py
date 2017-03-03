#!/usr/bin/python

# Originalliste
fr = ["Paris", "Lyon", "Marseille"]
print "Original:"
print fr

# Einsetzen eines Elementes
fr.insert(0,"Nantes")
print "Nach einsetzen:"
print fr

# Sortieren der Elemente
fr.sort()
print "Nach Sortieren:"
print fr

# umdrehen der Liste
fr.reverse()
print "Nach Umdrehen:"
print fr

# Entfernen eines Elementes
fr.remove("Nantes")
print "Nach entfernen:"
print fr

# Hinzufuegen eines Elementes
fr.append("Paris")
print "Hinzufuegen eines Elements:"
print fr

# Anzahl bestimmter Elemente
print "Anzahl Elemente Paris:", fr.count("Paris")

# Suchen bestimmter Elemente
print "Erste Position Paris", fr.index("Paris")
