from scraper.ScrapingStrategy import ScrapingStrategy

class Scraper(object):
    scrapingStrategy = ScrapingStrategy()

    def setScrapingStrategy(self, strategyToBeSet):
        self.scrapingStrategy = strategyToBeSet

    def doScrape(self, source, sourceName):
        self.scrapingStrategy.scrape(source, sourceName)