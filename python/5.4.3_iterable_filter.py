#!/usr/bin/python

# Funktion mit einem Parameter
def test(a):
    if a > 3:
        return True
    else:
        return False

# Funktion mit einem Parameter mehrmals aufrufen
x = [5, 6, -2, 0, 12, 3, -5]
z = filter(test,x)

# Ausgabe der Werte, die True ergeben
for element in z:
    print "True:", element
print
