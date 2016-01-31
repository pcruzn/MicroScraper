'''
@author: Pablo Cruz Navea

This module implements a client that tests the server by calling the remote function.

'''
import pika
import uuid

class MicroScraperClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host = 'localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive = True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.onResponse, no_ack = True,
                                   queue=self.callback_queue)

    
    # warning: correlationId belongs to the the requestor; correlation_id belongs to properties
    def onResponse(self, ch, method, properties, body):
        if self.correlationId == properties.correlation_id:
            self.response = body

    def callRemoteFunction(self, remoteFunctionParameter):
        # initially, 
        self.response = None
        
        # a random uuid used for the correlation id 
        self.correlationId = str(uuid.uuid4())
        
        self.channel.basic_publish(exchange='',
                                   routing_key='scraper_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.correlationId,
                                         ),
                                   body=str(remoteFunctionParameter))
        
        # date events are processed while no response received
        while self.response is None:
            self.connection.process_data_events()
        
        # this return is local; not to be confused with the value returned
        # by the remote function
        return int(self.response)

rpc_client = MicroScraperClient()

# for now, calle remote function with parameter 0 (actually, any value)
response = rpc_client.callRemoteFunction(0)

# print the remote procedure response
print("RP response: %r" % response)