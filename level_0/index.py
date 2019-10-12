#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

i = 0
d = {'id': 899, 'holdthedoor': 'Enviar consulta'}
url = "http://158.69.76.135/level0.php"

for i in range(1024):
    page = requests.post(url, data=d)
