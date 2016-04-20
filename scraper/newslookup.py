'''
Created on 10-03-2016

@author: Pablo Cruz Navea
'''

from bs4 import BeautifulSoup
import requests

r  = requests.get("http://www.elmostrador.cl")

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

for high_impact_article in soup.find_all("img"):
    print (high_impact_article.get('alt'))

for link in soup.find_all('a'):
    print(link.get('href'))