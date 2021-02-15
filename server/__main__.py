import threading

from server import init_api

app, socketio = init_api()


def test(msg):
    print(msg)
    socketio.emit('botResponse', msg)


def main():
    from server.message_broker.consumer import run
    consumer_message = threading.Thread(target=run, name='Consumer message')
    consumer_message.start()
    socketio.run(app, debug=True, host='localhost', port=5000)


if __name__ == '__main__':
    main()
