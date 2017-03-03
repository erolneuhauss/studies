#!/usr/bin/python

for i in range(48, 58):
    print chr(i), # Das Komma verhindert den Zeilenumbruch
print 

zahlen = ""
for i in range(48, 58):
#    zahlen += chr(i) + " " # Das Gleiche wie oben mit Variablenzuweisung
    zahlen += chr(i)
print zahlen

capitals = ""
for i in range(65, 91):
    capitals += chr(i)
print capitals

minors = ""
for i in range(97, 123):
    minors += chr(i)
print minors

for z in "Robinson":
    print ord(z),
print

unicodes = ""
#text = "Robinson" 
#liste = list(text) # list(): How to split a string into array of characters 
liste = list("Robinson")
print liste

unicodes = ""
for item in list("Robinson"):
#    unicodes += str(item), " "
#TypeError: cannot concatenate 'str' and 'tuple' objects
    unicodes += str(item) + " "
print unicodes

# statt das untere Konstrukt, haette ein Komma greicht:
# print ord(z), # siehe weiter oben
# print 
unicodes = ""
for item in list("Robinson"):
    unicodes += str(ord(item)) + " "
print unicodes

unicodes = ""
for item in list("Robinson"):
    unicodes += str(chr(ord(item)+1)) + " " # Wie Caesar mit den Generaelen
print unicodes
