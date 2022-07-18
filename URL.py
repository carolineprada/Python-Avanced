# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:28:15 2021

@author: Caroline
"""

#Import
from bs4 import BeautifulSoup
import requests


#url = raw_input ("Escribe el sitio web: ")

r = requests.get("https://www.google.com.co/imghp?hl=es&authuser=0&ogbl")

data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('img', class_="attachment-home-post wp-post-image"):
    print(link.get('width'))