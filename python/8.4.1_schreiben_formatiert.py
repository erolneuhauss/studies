#!/usr/bin/python3

import sys

# Zugriffsversuch
try:
    d = open("obst.txt", "w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Tabelle mit verschiedenen Objekten
fm = "{0:04d}{1:>12}{2:4d}{3:8.2f} Euro{4:8.2f} Euro\n"
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl  = {23:1,       8:3,        42:5}
epreis  = {23:2.95,    8:1.45,     42:3.05}

# Formatierung von Zeichenketten
d.write("{0:>4}{1:>12}{2:>4}{3:>13}{4:>13}\n".format
      ("Nr","Name","Anz","EP","GP"))

for x in 23, 8, 42:
    d.write(fm.format(x, artname[x], anzahl[x], epreis[x],
        anzahl[x] * epreis [x]))

# Schliessen der Datei
d.close()
