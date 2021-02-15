from datetime import datetime

from flask import jsonify

from server.__main__ import app
from server.configuration import config
from server.model.message import Message
from server.repository import user_repository
from server.request import stooq_requests


def retrieve_stooq_data(stooq_code):
    result = stooq_requests.get_to_stooq(stooq_code)
    msg = ''
    for record in result:
        if 'Symbol' not in record:
            msg = f'{record[0]} quote is ${record[6]} per share'

    user = user_repository.find_user_bot(config.CHAT_USER, config.CHAT_PASS)
    message = Message()
    message.message = msg
    message.date_time = datetime.now()
    message.user = user

    message_dto = Message.convert_model_to_dto(message)
    with app.app_context():
        response = jsonify(message_dto)
    return response.json
