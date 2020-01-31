#!/usr/bin/python

# Modul import importieren
import random,time

# initialisieren
random.seed()
# Anzahl richtiger Ergebnisse
richtig = 0
startzeit = time.time()

# Schleife mit "anzahl" Aufgaben
print "Start des Rechenspiels:",\
    time.strftime("%d.%m.%Y %H:%M:%S")
print

for aufgabe in range(5):
    # Aufgabe mit Ergebnis
    a = random.randint(10,30)
    b = random.randint(10,30)
    c = a + b
    print "Aufgabe:", aufgabe + 1,\
    "von 5:", a, "+", b

# Eingabe
    try:
        zahl = int(input("Bitte eine Zahl eingeben: "))
        if zahl == c:
            print zahl, "ist richtig"
            richtig += 1
        else:
            raise
    except:
        print "falsch"

# Auswertung
endzeit = time.time()
differenz = endzeit - startzeit
print "Richtig: {0:d} von 5 in {1:.2f} Sekunden".\
    format(richtig, differenz)
print "Ergebnis erzielt:",\
    time.strftime("%d.%m.%Y %H:%M:%S")
