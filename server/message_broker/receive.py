import time
from random import randrange

from server import channel
from server.__main__ import socketio
from server.service.stooq_service import retrieve_stooq_data


def callback(ch, method, properties, body: bytes):
    print(" [x] Received %r" % body)
    msg = body.decode('utf-8')
    if msg.startswith('/stock='):
        stock_code = msg.split('=')
        message_json = retrieve_stooq_data(stock_code[1])
        socketio.emit('botResponse', message_json, namespace='/bot')
    time.sleep(randrange(0, 5))
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_consuming():
    channel.queue_declare(queue='stock_msg')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume('stock_msg', callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
