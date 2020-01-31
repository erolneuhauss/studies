#!/usr/bin/python

# Moduael importieren
import time, thread

# Thread-Funktion
def show():
    global counter
    id = thread.get_ident()
    for i in range(5):
        counter += 1
        print i, id, counter

# Division durch 0
        if counter == 5:
            erg = 1 / 0
        time.sleep(1.5)
    return

# Hauptprogramm
id = thread.get_ident()
counter = 0
print id, counter

thread.start_new_thread(show,())
time.sleep(0.5)
thread.start_new_thread(show,())
time.sleep(10)

counter += 1
print id, counter
