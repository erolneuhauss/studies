#!/usr/bin/python
import time

# Zeit in Sekunden
print "Zeit in Sekunden", time.time()

# Akutelle, lokale Zeit als Tupel
lt = time.localtime()
print lt

# Entpacken des Tupel
# Datum
jahr, monat, tag = lt[0:3]
print "Datum: {0:02d}.{1:02d}.{2:4d}".\
    format(tag, monat, jahr)

# Uhrzeit
stunde, minute, sekunde = lt[3:6]
print "Uhrzeit: {0:02d}:{1:02d}:{2:02d}".\
    format(stunde, minute, sekunde)

# Wochentag
wtage = ["Montag","Dienstag","Mittwoch",\
    "Donnerstag","Freitag","Samstag","Sonntag"]
wtagnr = lt[6] 
print "Tag:", wtage[wtagnr]

# Tag des Jahres
tag_des_jahres = lt[7]
print "Der {0:d}. Tag des Jahres".format(tag_des_jahres)

# Sommerzeit
dst = lt[8]
if dst == 1:
    print "Sommerzeit"
elif dst == 0:
    print "Winterzeit"
else:
    print "Bestimmung nicht moeglich"
