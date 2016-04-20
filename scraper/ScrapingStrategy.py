'''
Created on 14-04-2016

@author: Pablo Cruz Navea
'''
from scraper.ElMostradorScraper import ElMostradorScraper
from scraper.EmolScraper import EmolScraper

class ScrapingStrategy(object):
    @staticmethod
    def scrape(source):
        raise NotImplementedError()
        
        
class EmolScrapingStrategy(ScrapingStrategy):
    @staticmethod
    def scrape(source):
        return EmolScraper.scrapeEmol(source)
    
class ElMostradorScrapingStrategy(ScrapingStrategy):
    @staticmethod
    def scrape(source):
        return ElMostradorScraper.scrapeElMostrador(source)