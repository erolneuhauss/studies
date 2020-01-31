#!/usr/bin/python
import time

# Geburtstag
dztupel = 1975, 10, 10, 0, 0, 0, 0, 0, 0

print "Geburt:", time.strftime\
    ("%d.%m.%Y", dztupel)
geburt = time.mktime(dztupel)
# print geburt # Angabe in Sekunden seit 1970-01-01
ltgeburt = time.localtime(geburt)

# Aktuell
ltheute = time.localtime()
print ltheute
 
print "Heute: ", time.strftime\
    ("%d.%m.%Y", ltheute)

# Alter berechnen
# print "Alter:", ltheute[0] - ltgeburt[0] # Hier wuerde man bloss die Differenz der Jahreszahlen bilden und Monate und Tage ausser Acht lassen

alter = ltheute[0] - ltgeburt[0] 
if ltheute[1] < ltgeburt[1] or\
    ltheute[1] == ltgeburt[1] and \
    ltheute[2] < ltgeburt[2]:
    alter = alter - 1
else:
    alter = alter
print "Alter:", alter

monate = ltheute[1] - ltgeburt[1] 
if ltheute[1] < ltgeburt[1] or\
    ltheute[1] == ltgeburt[1] and \
    ltheute[2] < ltgeburt[2]:
    monate = monate + 12
else:
    montate = monate
print "Monate:", monate

tage = ltheute[2] - ltgeburt[2] 
if ltheute[2] < ltgeburt[2] or\
    ltheute[2] == ltgeburt[2] and \
    ltheute[3] < ltgeburt[3]:
    tage = tage + 30
else:
    tage = tage
print "Tage:", tage

# print heute_sek
# print geburt

#heute_sek = time.mktime(ltheute)
#diff_jahre = (heute_sek - geburt)/60.0/60.0/24.0/365
#print "Alter in Jahren:  ", diff_jahre
#diff_wochen = (heute_sek - geburt)/60.0/60.0/24.0/7
#print "Alter in Wochen:  ", diff_wochen
#diff_tage = (heute_sek - geburt)/60.0/60.0/24.0
#print "Alter in Tagen:   ", diff_tage
#diff_stunden = (heute_sek - geburt)/60.0/60.0
#print "Alter in Stunden: ", diff_stunden
