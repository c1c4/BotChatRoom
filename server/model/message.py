from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from server import db
from server.model.user import User


class Message(db.Model):
    __tablename__ = 'tb_message'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('tb_user.id'), nullable=False)
    user = relationship('User')
    date_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    message = Column(String, nullable=False)

    @staticmethod
    def convert_model_to_dto(message_model):
        user_json = {
            'id': message_model.id,
            'dateTime': message_model.date_time.strftime('%d/%m/%Y %H:%M:%S'),
            'message': message_model.message,
            'user': User.convert_model_to_dto(message_model.user)
        }

        return user_json
