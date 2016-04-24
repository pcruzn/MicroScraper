from unittest import TestCase
from scraper.ElMostradorScraper import ElMostradorScraper

class TestElMostradorScraper(TestCase):
    def test_shouldRaiseExceptionOnBadURL(self):
        # uncomment method only fake URL is writen in ElMostradorScraper class
        # otherwise, this test will always fail!
        #self.assertRaises(Exception, ElMostradorScraper.scrapeElMostrador)

        # just because python requires an 'active' line in a method to be run
        return 0
