from io import StringIO
from unittest import TestCase

import sys

from scraper.GenericScrapingStrategy import GenericScrapingStrategy

class TestGenericScrapingStrategy(TestCase):
    def test_shouldPrintExceptionOnBadURL(self):
        GenericScrapingStrategy().scrape("http://www.laterce", "name")
        GenericScrapingStrategy().scrape("latercera", "name")

    def test_shouldSaveTextOnGoodURLAndConnection(self):
        GenericScrapingStrategy().scrape("http://www.emol.com", "Emol")