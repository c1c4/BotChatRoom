from flask import Blueprint, jsonify

from server.service.stock_service import retrieve_stock_data

stock_blueprint = Blueprint('messages_urls', __name__)


@stock_blueprint.route('/search-stock/<stock_code>', methods=['GET'])
def get_last_fifty_messages(stock_code):
    retrieve_stock_data(stock_code)
    return jsonify('OK'), 200
