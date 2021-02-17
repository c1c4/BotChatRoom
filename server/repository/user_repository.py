from server.model.user import User


def find_user_bot(user_name: str, password: str):
    return User.query.filter(User.user_name == user_name, User.password == password).first()
