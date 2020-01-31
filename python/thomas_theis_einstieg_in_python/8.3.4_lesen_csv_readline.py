#!/usr/bin/python

# Module importieren
import sys

# Zugriffversuch
try:
    d = open("daten.csv","r")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen als Ganzes 
einezeile = d.readline()

# Schliessen der Datei

# Jede Zeile umwandeln in Liste von int, string, float
li = []
while einezeile:
    zwliste = einezeile.split(";")
    li.append([int(zwliste[0]),
    zwliste[1],
    float(zwliste[2].replace(",", "."))])
    einezeile = d.readline()
print(li)

d.close()

for p in li:
    print("{0:d} {1} {2:.2f}".format(p[0], p[1], p[2]))
