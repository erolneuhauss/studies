#!/usr/bin/python

# Berechnung einer Summe
summe = 0
for i in range(1, 4):
    fehler = True
    while fehler:
#        zahl = raw_input(int(i) + ". Zahl eingegeben: ") # TypeError: unsupported operand type(s) for +: 'int' and 'str' 
        zahl = raw_input(str(i) + ". Zahl eingegeben: ") #   um mit dem restlichen Kommentar verkettet werden zu koennen, muss die Zahl in                                                             eine Zeichenkette umgewandelt werden
        try:
            summe += float(zahl)
            fehler = False
        except:
            print "Das war keine Zahl"
            fehler = True
print "Summe:", summe

# Geographiespiel
hauptstadt = {"Italien":"Rom", "Spanien":"Madrid", \
    "Portugal":"Lissabon"}

# siehe 4.5.3_dictionary_view.py fuer unterschiede zwischen items, values und keys
hs = hauptstadt.items()

for land, stadt in hs:
    eingabe = raw_input("Bitte die Hauptstadt von " \
        + land + " eingeben: ")
    if eingabe == stadt:
        print "richtig"
    else:
        print "falsch! Richtig ist:", stadt
