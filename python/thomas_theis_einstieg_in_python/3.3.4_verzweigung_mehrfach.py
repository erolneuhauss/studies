#!/usr/bin/python

print "Geben Sie bitte eine ganze Zahl ein", \
"Die Zahl darf negativ oder auch eine 0 sein"

# Benutzereingabe
x = raw_input()

# Ganze Zahl
gx = int(x)

# Ausgabe
print "x:", gx

if gx > 0:
	print "Diese Zahl ist positiv"
elif gx < 0:
	print "Diese Zahl ist negativ"
else:
	print "Diese Zahl ist gleich 0"
