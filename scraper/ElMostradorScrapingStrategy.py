from scraper.ScrapingStrategy import ScrapingStrategy
from bs4 import BeautifulSoup
import requests
from sqldb.SQLDB import SQLDBService

class ElMostradorScrapingStrategy(ScrapingStrategy):
    def scrape(self, source, sourceName):
        # ElMostrador scraper does not really requires source!
        r = requests.get("http://www.elmostrador.cl")

        html_doc = r.text

        soup = BeautifulSoup(html_doc, 'html.parser')

        for high_impact_article in soup.find_all("img"):
            if len(high_impact_article.get('alt')) > 50:
                print high_impact_article.get('alt')
                SQLDBService.storeTemporaryEncounter(
                    high_impact_article.get('alt').replace(u'\u201c', '"').replace(u'\u201d', '"'),
                    sourceName)