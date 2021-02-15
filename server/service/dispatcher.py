from server import __main__
from server.service.stooq_service import retrieve_stooq_data


def dispatch_msg_to_websocket(msg):
    message_json = retrieve_stooq_data(msg)
    __main__.test(message_json)
