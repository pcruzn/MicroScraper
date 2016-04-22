'''
Created on 18-04-2016

@author: Pablo Cruz Navea
'''

import sys

from scraper.EmolScraper import EmolScraper

try:
    EmolScraper.scrapeEmol()
except:
    print "Unexpected error: ", sys.exc_info()[0]

