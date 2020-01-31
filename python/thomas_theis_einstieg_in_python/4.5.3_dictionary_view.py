#!/usr/bin/python

# Erzeugung eines Dictionarys
alter = {"Peter":31, "Julia":28, "Werner":35}

# Werte
werte = alter.values()
for value in werte:
    print value
print "Anzahl der Werte:", len(werte)

# Elemente enthalten?
if 31 in werte:
    print "31 ist enthalten!"

alter["Peter"] = 41
if 31 not in werte: # das funzt mit python3 nicht, da in 2.7 views nicht aktualisiert werden
    print "31 ist nicht enthalten"

for personen in alter:
    print personen, alter[personen]

# Keys
k = alter.keys()

print "Anzahl der Keys:", len(k)
for x in k:
    print x

if "Werner" in k:
    print "Werner ist enthalten"

del alter["Werner"]
if "Werner" not in k: # das funzt mit python3 nicht, da in 2.7 views nicht aktualisiert werden
    print "Werner ist nicht enthalten"

# Items
i = alter.items()
alter["Franz"] = 35  # das funzt mit python3 nicht, da in 2.7 views nicht aktualisiert werden
print "Anzahl der Items:", len(i)
for x in i:
    print x

if ("Julia", 28) in i:
    print "Julia, 28 ist enthalten"

# Noch ein Beispiel, um items, values und keys zu verdeutlichen:

hauptstadt = {"Italien":"Rom", "Spanien":"Madrid", \
    "Portugal":"Lissabon"}

for land in hauptstadt:
    print land

hs = hauptstadt.items()

for land in hs:
    print land

for land, stadt in hs:
    print land, stadt

hs = hauptstadt.values()

for staedte in hs:
    print staedte

hs = hauptstadt.keys()

for staedte in hs:
    print staedte
