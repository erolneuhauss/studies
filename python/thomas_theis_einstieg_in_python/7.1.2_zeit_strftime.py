#!/usr/bin/python
import time

# Akutelle, lokale Zeit als Tupel
lt = time.localtime()
print lt
print

print time.strftime\
    ("Tag.Monat.Jahr: %d.%m.%Y", lt)
print time.strftime\
    ("Hours.Minutes.Seconds: %H.%M.%S", lt)
print time.strftime\
    ("Im 12-Stunden-Format: %I.%M.%S Uhr %p", lt)
print time.strftime\
    ("Datum und Zeit: %c", lt)
print time.strftime\
    ("Jahr in zwei Ziffern: %y", lt)
print time.strftime\
    ("Tag des Jahres: %j", lt)
print

# Woche, Monat
print time.strftime\
    ("Wochentag kurz: %a, ganz:%A, Nr.(Sonntag=0):%w", lt)
print time.strftime\
    ("Monat kurz:%b, ganz:%B", lt)
print

# Kalenderwoche
print time.strftime\
    ("KW (Beginn Sonntag): %U", lt)
print time.strftime\
    ("KW (Beginn Montag): %W", lt)
print

print time.strftime\
    ("Zeitzone: %Z", lt)
