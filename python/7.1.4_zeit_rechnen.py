#!/usr/bin/python
import time

# Zwei Zeitangabe erzeugen
dztupel1 = 1979, 2, 15, 23, 55, 0, 0, 0, 0
#print dztupel1

damals1 = time.mktime(dztupel1)
print "Zeit 1:", time.strftime\
    ("%d.%m.%Y %H:%M:%S", dztupel1)

dztupel2 = 1979, 2, 16, 0, 5, 15, 0, 0, 0
#print dztupel2

damals2 = time.mktime(dztupel2)
print "Zeit 2:", time.strftime\
    ("%d.%m.%Y %H:%M:%S", dztupel2)

# Differenz berechnen
print "Differenz:"

diff_sek = damals2 - damals1
print diff_sek, "Sekunden"

diff_min = diff_sek / 60.0
print diff_min, "Minuten"

diff_std = diff_min / 60.0
print diff_std, "Stunden"

diff_tag = diff_std / 24.0
print diff_tag, "Tage"
