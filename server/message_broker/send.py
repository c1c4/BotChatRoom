from kombu import Connection, Exchange, Queue, Producer


def send_stock_message(msg):
    rabbit_url = "amqp://localhost:5672/"

    conn = Connection(rabbit_url)

    channel = conn.channel()

    exchange = Exchange("stock-exchange", type="direct")

    producer = Producer(exchange=exchange, channel=channel, routing_key="stock")

    queue = Queue(name="stock-queue", exchange=exchange, routing_key="stock")
    queue.maybe_bind(conn)
    queue.declare()

    producer.publish(msg)
