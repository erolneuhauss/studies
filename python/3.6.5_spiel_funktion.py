#!/usr/bin/python
# Aufgabe, in der das Ergebnis als Rückgabewert in erg gespeichert wird
def aufgabe():
    a = random.randint(1,10)
    b = random.randint(1,10)
    erg = a + b
    print "Die Aufgabe:", a, "+", b
    return erg

# Kommentar mit Verzweigung
def kommentar(eingabezahl,ergebnis):
    if eingabezahl == ergebnis:
        print eingabezahl, "ist richtig"
    else:
        print eingabezahl, "ist falsch"

# Modul import importieren
import random

# Zufallsgenerator initialisieren
random.seed()

# Aufgabe
# die Variable c erhält den Rückgabewert aus der Variable erg der Fkt. aufgabe()
# der Rückgabewert wird in c zwischengespeichert und an anderer Stelle gebraucht
c = aufgabe() 
# print c # um zu schauen, was der Rückgabewert ist.

# Schleife initialisieren
zahl = c + 1

# Anzahl initialisieren
versuch = 0

# Schleife mit while
while zahl != c:
# Anzahl Versuche zaehlen
    versuch += 1 
    print "Bitte rechnen und Ergebnis eingeben"		
    z = raw_input()
    try:
        zahl = int(z)
    except:
# Falls Umwandlung nicht erfolgreich
        print "Sie haben keine Zahl eingegeben"
# Schleife unmittelbar fortsetzen und nicht abbrechen oder dergleichen
        continue

# Kommentar
    kommentar(zahl,c)

# Anzahl ausgeben
print "Das Ergebnis:", c
print "Anzahl Versuche:", versuch
