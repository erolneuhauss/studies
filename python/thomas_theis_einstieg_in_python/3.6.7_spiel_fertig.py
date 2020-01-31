#!/usr/bin/python

# Modul import importieren
import random

# Zufallsgenerator initialisieren
random.seed()

# Anzahl Aufgaben
anzahl = -1
while anzahl < 0 or anzahl > 10:
    try:
        print "Wie viele Aufgaben (1 bis 10)?"
        anzahl = int(raw_input())
    except:
        continue

# Anzahl richtiger Ergebnisse
richtig = 0

# Schleife mit "anzahl" Aufgaben
for aufgabe in range(1,anzahl+1):
    # Operatorauswahl
    opzahl = random.randint(1,4)
    if opzahl == 1:
        a = random.randint(-10,30)
        b = random.randint(-10,30)
        op = "+"
        c = a + b
    elif opzahl == 2:
        a = random.randint(1,30)
        b = random.randint(1,30)
        op = "-"
        c = a - b
    elif opzahl == 3:
        a = random.randint(1,10)
        b = random.randint(1,10)
        op = "*"
        c = a * b
    elif opzahl == 4:
#        a = random.randint(1,10) # statt a c, damit nur ganze Zahlen zustande kommen
        c = random.randint(1,10)
        b = random.randint(1,10)
        op = "/"
#        c = a / b # in der Aufgabe soll man nicht so teilen
#        c = a / b | * b # umstellen
#        c * b = a # das gleiche wie unten
        a = c * b

# Aufgabenstellung
    print "Die Aufgabe:", aufgabe, "von", \
    anzahl, ":", a, op, b

# Schleife mit drei Versuchen
    for versuch in range(1,4):
        try:
            print "Bitte eine Zahl eingeben"
            zahl = int(raw_input())
        except:
# Falls Umwandlung nicht erfolgreich
            print "Sie haben keine Zahl eingegeben"
# Schleife unmittelbar fortsetzen und nicht abbrechen oder dergleichen
            continue
            
# Kommentar mit Verzweigung
        if zahl == c:
            print zahl, "ist richtig"
            richtig += 1
            break
        else:
            print zahl, "ist falsch"
# Anzahl ausgeben
    print "Das Ergebnis:", c
print "Richtig:", richtig, "von", anzahl
