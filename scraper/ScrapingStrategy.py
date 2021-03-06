'''
Created on 14-04-2016

@author: Pablo Cruz Navea
'''
from abc import ABCMeta, abstractmethod

# we use an abstract class instead of interface (as they do not really exist in python)
class ScrapingStrategy(object):

    @abstractmethod
    def scrape(self, source, sourceName):
        raise NotImplementedError()