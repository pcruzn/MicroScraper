'''
Created on 13-03-2016

@author: Pablo Cruz Navea
'''
#!/usr/bin/env python
import pika
import sys
from scraper.ElMostradorScraper import ElMostradorScraper
from scraper.EmolScraper import EmolScraper

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_scraping_queue')

def scrape(source):
    status = 1
    if source == "ElMostrador":
        try:
            ElMostradorScraper.scrapeElMostrador()
        except:
            print "Unexpected error: ", sys.exc_info()[0]
            status = 2
    
    if source == "Emol":
        try:
            EmolScraper.scrapeEmol()
        except:
            print "Unexpected error: ", sys.exc_info()[0]
            status = 2

    # on success, return 1!, on any error, return 2
    return status


def on_request(ch, method, props, body):
    source = body

    print("A scraping request for %s has arrived" % source)
    response = scrape(source)

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