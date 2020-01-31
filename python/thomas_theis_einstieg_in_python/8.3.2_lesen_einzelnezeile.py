#!/usr/bin/python

# Module importieren
import sys

# Zugriffversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen und Ausgabe einzelner Zeilen
zeile1 = d.readline() 
print(zeile1, end="") # da jede Zeile bereits das Zeilenende-Zeichen enthält, muss dieses abgeschnitten werden

zeile2 = d.readline() 
print(zeile2, end="")

# Summe und Ausgabe
summe = float(zeile1) + float(zeile2)
print("Summe:", summe)

# Schliesen einer Datei
d.close()
