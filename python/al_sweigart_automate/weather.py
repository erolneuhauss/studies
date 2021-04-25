#!/usr/bin/env python
import argparse
import os
import sys
from pprint import pprint

import requests

parser = argparse.ArgumentParser(
    description="Get the current weather information for your zipcode"
)
parser.add_argument("--zip", help="zip/postal code to get weather for", default="51143")
parser.add_argument(
    "--country",
    default="DE",
    help="DE or any other country code, defaults to DE for Germany",
)
parser.add_argument(
    "--units", default="metric", help="metric or imperial, defaults to metric"
)
parser.add_argument(
    "--language",
    default="de",
    help='"de" or any other language code, defaults to de for german',
)


args = parser.parse_args()
# print(args)

api_key = os.getenv("OWM_API_KEY")
if not api_key:
    print("Error: no 'OWM_API_KEY' provided.")
    sys.exit(1)

# print(api_key)

url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&units={args.units}&lang={args.language}&appid={api_key}"

# print(url)
res = requests.get(url)
# print(res)

if res.status_code != 200:
    print(f"Error talking to weather provider: {res.status_code}")
    sys.exit(1)

data = res.json()
# pprint(data)

zip = data["name"]
temp = data["main"]["temp"]
wind_speed = round(data["wind"]["speed"] * 100 / 60, 1)
description = data["weather"][0]["description"]
rain = "☔"
sun_cloud = "⛅"
sun = "🌞"

print(" ⛅ ".center(30, "-"))
print(f"Ort: {zip}")
print(f"Temp: {temp}°C")
print(f"Wind: {wind_speed} km/h")
print(f"Lage: {description}")
print(" ⛅ ".center(30, "-"))
