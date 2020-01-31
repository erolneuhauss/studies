#!/usr/bin/python

# 1: Zahl mit Nachkommastellen
x = 100 / 7.0
y = 2 / 7.0

print "Zahlen:"
print x, y
print

# 2: Format f
print "Format f"
print "{0:f} {0:f} {1:f}".format(x,y)
print "{0:15.10f} {1:.25f}".format(x,y)
print

# 3: Format e
print "Format e"
print "{0:e}".format(x,y)
print "{0:12.3e}".format(x,y)
print "{0:.3e}".format(x,y)
print

# 4: Format %
print "Format %"
print "{0:%}".format(y)
print "{0:12.3%}".format(y)
print "{0:.3%}".format(y)
print
