'''
@author: Pablo Cruz Navea

This module implement a simple 'server' with an empty 'remote function' called
scraping. That function will return the results gathered by scrapy.

'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host = 'localhost'))

channel = connection.channel()

# queue is called 'scraper_queue'
channel.queue_declare(queue = 'scraper_queue')

# the remote procedure (i.e., the procedure implemented in the server)
def scraping(n):
    return 0
    

def onRequest(ch, method, props, body):
    # here it is the value passed as argument to the 'remote function' (scraping up to now)
    n = int(body)

    print("Received: %s" % n)
    
    response = scraping(n)

    ch.basic_publish(exchange = '',
                     routing_key = props.reply_to,
                     properties = pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body = str(response))
    
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count = 1)

channel.basic_consume(onRequest, queue = 'scraper_queue')

print("Waiting for calls...")

channel.start_consuming()