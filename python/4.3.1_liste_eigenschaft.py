#!/usr/bin/python

# Liste von Zahlen
z = [3, 6, 12.5, -8, 5.5]
print "print z", "entspricht", z
print "print z[0]", "entspricht", z[0]
print "print z[0:3]", "entspricht", z[0:3]

# Liste von Zeichenketten
cities = ["Hamburg", "Augsburg", "Berlin"]
print cities

# Anzahl Elemente
print "Anzahl:", len(cities)

# list indices must be integers, not str
# object in a for loop must be iterable

print 'cities = ["Hamburg", "Augsburg", "Berlin"]'

# Lehrbuchmethode
elements_via_range_index = """
for counter in range(0,len(cities)): 
    print counter, cities[counter]
"""
print elements_via_range_index
for counter in range(0,len(cities)): # Anzahl eventuell unbekannt - muss vorher ermittelt werden
    print counter, cities[counter]

# Alternativen
elements_via_index = """
for city in cities[0:3] 
    print city
"""
print elements_via_index
for city in cities[0:3]:
    print city
# oder einfacher:
elements_direct = """
for city in cities:
    print city
"""
print elements_direct 
for city in cities:
    print city
