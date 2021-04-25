#!/usr/bin/env python
"""Download and select price for certain course"""
import bs4
import requests


def get_course_price(product_url):
    """Returns price for given URL"""
    res = requests.get(product_url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select("span.current-price")
    return elems[0].text


SCHEME = "https://"
DOMAIN = "school.scientificprogramming.io/"
PATH = "home/course/linux-network-administration/16"
URL = SCHEME + DOMAIN + PATH
PRICE = get_course_price(f"{URL}")
print(f"The price is {PRICE}")
