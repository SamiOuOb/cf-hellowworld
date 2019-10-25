import pika

def send_data():
    #連接RMQ
    user = 'e7b55c23-4fa9-4a0f-8fe0-78f6a4af96d6'
    password = 'lEPdudGipfXRByd8SPm3dh6zs'
    host='10.10.0.13'
    vhost='2bbeda0a-a8c4-4c53-848f-4c23573d5f30'


    #RMQ參數定義
    exchange = 'hello_exchange'
    routing_key = 'hello_rk'

    rabbitmq_uri = 'amqp://{}:{}@{}:5672/{}'.format(user, password, host, vhost)
    connection = pika.BlockingConnection(pika.connection.URLParameters(rabbitmq_uri))
    channel = connection.channel()

    channel.basic_publish(exchange=exchange, routing_key=routing_key, body='Hello World', 
                            properties=pika.BasicProperties(delivery_mode = 2))

    