'''
Created on 13-03-2016

@author: Pablo Cruz Navea
'''
#!/usr/bin/env python
import pika
import sys

from broker.APIHelpers import RPCParameterHelper
from scraper.EmolScrapingStrategy import EmolScrapingStrategy
from scraper.GenericScrapingStrategy import GenericScrapingStrategy
from scraper.Scraper import Scraper
from scraper.ElMostradorScrapingStrategy import ElMostradorScrapingStrategy

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_scraping_queue')

def scrape(source, sourceName):
    status = 1

    #scrape ElMostrador
    if source == "ElMostrador":
        scraper = Scraper()
        scraper.setScrapingStrategy(ElMostradorScrapingStrategy())
        try:
            scraper.doScrape(source, "ElMostrador")
        except:
            print "Unexpected error: ", sys.exc_info()[0]
            status = 2
    # scrape Emol
    elif source == "Emol":
        scraper = Scraper()
        scraper.setScrapingStrategy(EmolScrapingStrategy())
        try:
            scraper.doScrape(source, "Emol")
        except:
            print "Unexpected error: ", sys.exc_info()[0]
            status = 2
    # scrape generic!
    else:
        scraper = Scraper()
        scraper.setScrapingStrategy(GenericScrapingStrategy())
        try:
            scraper.doScrape(source, sourceName)
        except:
            print "Unexpected error: ", sys.exc_info()[0]
            status = 2


    # on success, return 1!, on any error, return 2
    return status


def on_request(ch, method, props, body):
    parametersList = RPCParameterHelper.splitParameters(body)

    print("A scraping request for %s has arrived" % parametersList[0])
    response = scrape(parametersList[0], parametersList[1])

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_scraping_queue')

print("Waiting MOAI request...")

channel.start_consuming()