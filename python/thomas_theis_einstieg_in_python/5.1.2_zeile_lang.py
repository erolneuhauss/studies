#!/usr/bin/python

print "Umrechnen von Celsius in Fahrenheit"

# Trennung einer Zeichenkette
print "Bitte geben Sie eine" \
    " Temperatur in Celsius ein: "
TemperaturInCelsius = float(raw_input())
TemperaturInFahrenheit = TemperaturInCelsius * 9 / 5.0 + 32

# Trennung nach einem Komma
print TemperaturInCelsius, "Grad Celsius entsprechen", \
    TemperaturInFahrenheit, "Grad in Fahrenheit"

# Alternativ, kuerzer, aber schwieriger nachzuvollziehen:

TemperaturInCelsius = float(raw_input("Bitte geben Sie eine Temperatur in Celsius ein:"))
print TemperaturInCelsius, "Grad Celsius entsprechen", \
    TemperaturInCelsius * 9 / 5.0 + 32, "Grad in Fahrenheit"
