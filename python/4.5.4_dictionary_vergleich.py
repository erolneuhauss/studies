#!/usr/bin/python

# Erzeugung von zwei Dictionarys
alter1 = {"Peter":31, "Julia":28}
alter2 = {"Julia":28, "Peter":31}

# Vergleich
if alter1 == alter2:
    print "Dictionaries sind gleich"

if alter1 < alter2: # Vergleich mit Python2.7 scheint moeglich zu sein, das Ergebnis hat keine definierte Aussage
    print "alter1 < alter2"
else:
    print "alter1 > | == alter2"
    
