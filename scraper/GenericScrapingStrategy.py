from bs4 import BeautifulSoup
import requests
from sqldb.SQLDB import SQLDBService

from scraper.ScrapingStrategy import ScrapingStrategy


class GenericScrapingStrategy(ScrapingStrategy):
    def scrape(self, source, sourceName):
        # assumption: url is ok!, but if not, then RequestException is caught
        try:
            r = requests.get(source)
        except requests.exceptions.RequestException as r_exception:
            print r_exception
            return 2

        html_doc = r.text

        soup = BeautifulSoup(html_doc, 'html.parser')

        # the generic scraper does only get all text from the source
        # in order to avoid uninteresting text, we only consider "text" above 50 characters length
        for genericSourceLinkText in soup.find_all("a"):
            if len(genericSourceLinkText.getText()) > 50:
                SQLDBService.storeTemporaryEncounter(
                        genericSourceLinkText.getText().replace(u'\u201c', '"').replace(u'\u201d', '"'),
                        sourceName)
