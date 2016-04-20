'''
Created on 10-03-2016

@author: Pablo Cruz Navea
'''

from bs4 import BeautifulSoup
import requests
from sqldb.SQLDB import SQLDBService

class EmolScraper(object):
    @staticmethod
    def scrapeEmol():
        r  = requests.get("http://www.emol.com")
        
        html_doc = r.text
        
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        for emol_link in soup.find_all("a"):
            if len(emol_link.getText()) > 50:
                SQLDBService.insertTemporaryEncounter(emol_link.getText(), "Emol")
