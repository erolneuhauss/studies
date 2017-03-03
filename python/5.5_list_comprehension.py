#!/usr/bin/python

# Zwei Beispiellisten
xliste = [3, 6, 8, 9, 15]
print xliste
yliste = [2, 13, 4, 8, 4]
print yliste
print

# Beispiel 1: Version ohne List Comprehension
aliste = []
for item in xliste:
    aliste.append(item + 1)
print aliste

# Beispiel 1: Version mit List Comprehension
aliste = [item + 1 for item in xliste]
print aliste
print

bliste=[]
for item in xliste:
    if item > 7:
        bliste.append(item + 1)
print bliste

bliste = [item + 1 for item in xliste if item > 7]
print bliste
print

xliste = [3, 6, 8, 9, 15]
yliste = [2, 13, 4, 8, 4]

cliste = []
for i in range(len(xliste)):
    if xliste[i] < 10 and yliste[i] < 10:
        cliste.append(xliste[i] * 10 + yliste[i])
print cliste

cliste = [xliste[i] * 10 + yliste[i]\
    for i in range(len(xliste))\
        if xliste[i] < 10 and yliste[i] < 10]
print cliste

