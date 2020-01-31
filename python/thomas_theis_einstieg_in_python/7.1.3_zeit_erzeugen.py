#!/usr/bin/python
import time

# Zeitangabe erzeugen
dztupel= 1979, 2, 15, 13, 0, 0, 0, 0, 0
print dztupel

print time.strftime\
    ("%d.%m.%Y %H:%M:%S", dztupel)
damals = time.mktime(dztupel)

# Ausgabe
lt = time.localtime(damals) 
print lt

# Wochentag
wtage = ["Montag","Dienstag","Mittwoch",\
    "Donnerstag","Freitag","Samstag","Sonntag"]
wtagnr = lt[6] 
print "Tag:", wtage[wtagnr]

# Tag des Jahres
tag_des_jahres = lt[7]
print "Der {0:d}. Tag des Jahres".format(tag_des_jahres)
