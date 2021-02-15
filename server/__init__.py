import pika
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

from server.configuration.exceptions import NotFound, generic_render, DataFail, Unauthorized, BusinessFail, \
    ApiBaseException, \
    error_notification_render

db = SQLAlchemy()
socketio = SocketIO()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


def init_api():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('configuration.config.Config')
    app.register_error_handler(NotFound, generic_render)
    app.register_error_handler(Unauthorized, generic_render)
    app.register_error_handler(BusinessFail, generic_render)
    app.register_error_handler(DataFail, generic_render)
    app.register_error_handler(ApiBaseException, error_notification_render)
    db.init_app(app)
    CORS(app)

    socketio.init_app(app, cors_allowed_origins="*")

    return app, socketio