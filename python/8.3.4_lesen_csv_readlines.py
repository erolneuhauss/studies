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
gesamtertext = d.readlines()

# Schliessen der Datei
d.close()

# Jede Zeile umwandeln in Liste von int, string, float
li = []
for zeile in gesamtertext:
    zwliste = zeile.split(";")
    li.append([int(zwliste[0]),
    zwliste[1],
    float(zwliste[2].replace(",", "."))])
print(li)

for p in li:
    print("{0:d} {1} {2:.2f}".format(p[0], p[1], p[2]))
