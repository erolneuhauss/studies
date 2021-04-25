#!/usr/bin/env python
"""Open given Address with python's requests module"""
import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

print(res.status_code)

print(len(res.text))
