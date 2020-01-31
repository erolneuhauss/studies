#!/usr/bin/python

# Module importieren
import sys

# Zugriffversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen des gesamten Textes
gesamtertext = d.read()
print(gesamtertext)

# Schliessen der Datei
d.close()

zeilenliste = gesamtertext.split(chr(10))
print(zeilenliste)

# Summieren und Ausgeben
summe = 0
for zeile in zeilenliste:
    if zeile:
        summe += float(zeile)
    print(zeile)

# Ausgabe der Summe
print("Summe:", summe)

#d.close()
