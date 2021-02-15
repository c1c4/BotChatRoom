import eventlet

from server import init_api

eventlet.monkey_patch()

app, socketio = init_api()


def main():
    from server.message_broker.receive import start_consuming
    start_consuming()
    socketio.run(app, debug=True)


if __name__ == '__main__':
    main()
