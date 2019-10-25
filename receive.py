#!/usr/bin/env python
import pika
def receive_data():
    #連接RMQ
    user = 'e7b55c23-4fa9-4a0f-8fe0-78f6a4af96d6'
    password = 'lEPdudGipfXRByd8SPm3dh6zs'
    host='10.10.0.13'
    vhost='2bbeda0a-a8c4-4c53-848f-4c23573d5f30'

    rabbitmq_uri = 'amqp://{}:{}@{}:5672/{}'.format(user, password, host, vhost)

    connection = pika.BlockingConnection(pika.connection.URLParameters(rabbitmq_uri))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)




    channel.basic_consume("hello_q1",
                 callback,
)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
receive_data()
