from server import init_api
from server.configuration import config
from server.controllers.stock_controller import stock_blueprint


def main():
    app = init_api()
    app.register_blueprint(stock_blueprint)
    app.run(debug=True, host=config.HOST, port=config.PORT)


if __name__ == '__main__':
    main()
