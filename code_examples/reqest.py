# -*- coding: utf-8 -*-

import requests

url = "https://httpbin.org/get"
response = requests.get(url)
with open("response.text.txt", "w", encoding="utf-8") as t:
    t.write(response.text)
