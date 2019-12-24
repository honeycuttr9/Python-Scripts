#!/usr/bin/env python

import requests
import re
from bs4 import BeautifulSoup

url = requests.get('https://www.yellowbook.com/s/seafood-restaurants/charleston-sc/')

#phoneNums = re.findall(r'(\d{3}(\s|[-]){1}\d{3}[-]{1}\d{4})', (url.text))
phoneNums = re.findall(r'([(]*\d{3}[)]*\s\d{3}[-|\s]{1}\d{4})', url.text)
print(phoneNums)
