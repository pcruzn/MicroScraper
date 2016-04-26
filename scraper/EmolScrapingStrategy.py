from scraper.ScrapingStrategy import ScrapingStrategy
from bs4 import BeautifulSoup
import requests
from sqldb.SQLDB import SQLDBService

class EmolScrapingStrategy(ScrapingStrategy):
    def scrape(self, source, sourceName):
        # Emol scraper does not really requires source!
        @staticmethod
        def scrapeEmol():
            r = requests.get("http://www.emol.com")

            html_doc = r.text

            soup = BeautifulSoup(html_doc, 'html.parser')

            for emol_link in soup.find_all("a"):
                if len(emol_link.getText()) > 50:
                    SQLDBService.storeTemporaryEncounter(emol_link.getText(), sourceName)