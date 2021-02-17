from datetime import datetime

from flask import jsonify

from server.configuration import config
from server.message_broker.send import send_stock_message
from server.model.message import Message
from server.repository import user_repository
from server.request import stooq_requests


def retrieve_stock_data(stooq_code):
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
    send_stock_message(message_dto)
