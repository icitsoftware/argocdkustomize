#!/usr/bin/env python
from time import sleep
import pika

credentials = pika.PlainCredentials("default_user_7k5BofUKMS4iDwwXvlZ","YLtBb2383Odqy402HukP8_O4tiJLhBYX")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",port=56579,credentials=credentials))
channel = connection.channel()

channel.exchange_declare('test', durable=True, exchange_type='topic')
channel.queue_declare(queue= 'A')
channel.queue_bind(exchange='test', queue='A', routing_key='A')
channel.queue_declare(queue= 'B')
channel.queue_bind(exchange='test', queue='B', routing_key='B')
channel.queue_declare(queue= 'C')
channel.queue_bind(exchange='test', queue='C', routing_key='C')
#messaging to queue named C
message= 'hello consumer!!!!!'
channel.basic_publish(exchange='test', routing_key='C', body= message)
channel.basic_publish(exchange='test', routing_key='C', body= message)
channel.basic_publish(exchange='test', routing_key='C', body= message)
channel.basic_publish(exchange='test', routing_key='C', body= message)
channel.basic_publish(exchange='test', routing_key='C', body= message)
channel.close()