#!/usr/bin/python3

import sys,os

# Zugriffsversuch
try:
    d = open("obst.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Gezieltes Lesen
for i in range(1,4):
    # Nr Lesen
    d.seek(47*i)
    nr = int(d.read(4))

    # EP lesen
    d.seek(20 + 47*i)
    ep = float(d.read(8))

    # Ausgabe
    print("Artikel Nr:", nr, ", EP:", ep)


d.close()
