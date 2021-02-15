from server.__main__ import app
from server.model.user import User


def find_user_bot(user_name: str, password: str):
    with app.app_context():
        return User.query.filter(User.user_name == user_name, User.password == password).first()
