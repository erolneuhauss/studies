#!/usr/bin/python

# Schleife mit range
for i in range(1,7):
    print "Zahl:", i
    if i >= 3 and i <= 5:
#    if 3 <= i <= 5: # funktionierende Alternative im Buch
        continue
    print "Quadrat:", i*i
