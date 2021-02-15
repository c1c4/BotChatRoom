from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from server import db


class User(db.Model):
    __tablename__ = 'tb_user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    url_avatar = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    @staticmethod
    def convert_dto_to_model(json_user):
        user = User()
        user.user_name = json_user['userName']
        user.password = json_user['password']
        user.email = json_user['email']

        return user

    @staticmethod
    def convert_model_to_dto(user_model):
        user_json = {
            'id': user_model.id,
            'userName': user_model.user_name,
            'email': user_model.email,
            'urlAvatar': user_model.url_avatar
        }

        return user_json
