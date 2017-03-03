#!/usr/bin/python

# Moduael importieren
import sys

# Zugriffversuch
try:
    d = open("lesen.txt")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Lesen aller Zeilen in eine Liste
allezeilen = d.readlines() # als Liste
#allezeilen = d.readline() # Zeilenweise, nur erste Zeile
#allezeilen = d.read() # komplett 1:1
print (allezeilen)

# Schliesen einer Datei
d.close()

# Ausgabe und Summierung der Listenelemente
summe = 0
for zeile in allezeilen:
    print(zeile, end="")
    summe += float(zeile)
# Ausgabe der Summe
print("Summe:", summe)
