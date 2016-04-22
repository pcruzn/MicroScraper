'''
Created on 10-03-2016

@author: Pablo Cruz Navea
'''

from bs4 import BeautifulSoup
import requests
from sqldb.SQLDB import SQLDBService

class ElMostradorScraper(object):
    @staticmethod
    def scrapeElMostrador():
        r  = requests.get("http://www.elmostrador.cl")
        
        html_doc = r.text
        
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        for high_impact_article in soup.find_all("img"):
            if len(high_impact_article.get('alt')) > 50 :
                print high_impact_article.get('alt')
                SQLDBService.insertTemporaryEncounter(high_impact_article.get('alt').replace(u'\u201c', '"').replace(u'\u201d', '"'),
                                                      "ElMostrador")
