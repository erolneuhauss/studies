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
#allezeilen = d.readline() # Zeilenweise
#allezeilen = d.read() # komplett 1:1
print (allezeilen)



# Schliesen einer Datei
d.close()
