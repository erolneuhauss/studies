#!/usr/bin/python

# Ausgabe einer for-schleife mit range

inch = 2.54
fmt = "{0:6.1f} {1:6.1f}"
head = "{0:>6} {1:>6}".format("inch", "cm")

print head
for i in range(15,45,5):
	print fmt.format(i, i * inch)
