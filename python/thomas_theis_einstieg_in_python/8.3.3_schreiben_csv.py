#!/usr/bin/python

# Module importieren
import sys

# Zugriffversuch
try:
    d = open("daten.csv","w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Schreiben einer Liste als CSV-Datensatz
li = [42, "Maier", 3524.52]
d.write(str(li[0]) + ";" + li[1] + ";" 
    + str(li[2]).replace(".",",") + "\n")

dli = [[55, "Werner", 3185.00], [57, "Schulz", 2855.20]]

for item in dli:
    d.write(str(item[0]) + ";"
        + item[1] + ";"
        + str(item[2]).replace(".",",") + "\n")

# Schliessen der Datei
d.close()
