#!/usr/bin/python

# Beispiel-Sequenz, hier Zeichenkette
tname = "Robinson Crusoe"
print "Text:", tname

# Anzahl der Elemente
lg = len(tname)
print "Anzahl Elemente:", lg

# Teilbereiche, Elemente
ts = tname[5:8]
print "[5:8]:", ts
ts = tname[:8]
print "[:8]:", ts
ts = tname[9:]
print "[9:]:", ts
ts = tname[9]
print "[9]:", ts
ts = tname[9:-3]
print "[9:-3]:", ts
