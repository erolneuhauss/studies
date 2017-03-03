#!/usr/bin/python

# 1: Mehrfach Zuweisung
x, y, z = 3, 5.2, "Hallo"
print "mehrfache Zuweisung:", x, y, z

# 2: Auswirkungen erst danach
print """
a = 12
b = 15
c = 22

a, b, c = c, a, a + b
"""

a = 12
b = 15
c = 22

a, b, c = c, a, a + b
print "Auswirkung:", a, b, c

# 3: Verpacken eines Tupels
p = 3, 4
print "verpackt:", p

# 4: Entpacken eines Tupels
m, n = p
print "entpackt: m:", m, "n:", n 

# 5: falsche Zuweisung eines Tupels
try:
    s, t = 3, 4, 12
    print s, t
except:
    print "ValueError: too many values to unpack"

# 6: Rest in Liste. funzt nicht mit Python 2.7, sondern erst mit Python 3
#print()
#x, *y, z = 3, 5.2, "hallo", 7.3, 2.9
#print x
#print y
#print z

