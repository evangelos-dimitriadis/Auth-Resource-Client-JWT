import bcrypt
import jwt
import logging
from sqlalchemy import Integer, String, Column
from extras import db
from datetime import datetime, timedelta


class User(db.Model):
    """A SQLAlchemy model that stores user details"""

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def encode_auth_token(self, user_id: int) -> str:
        """
        Generates the Auth Token
        :return: token on success
        :rtype: string
        :raises Exception: For every error
        """
        try:
            private_key = open('jwt-key').read()

            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, minutes=5),  # expiration
                'iat': datetime.utcnow(),  # issued at
                'sub': user_id  # subject
            }
            token = jwt.encode(payload, private_key, algorithm='RS256')
            return token
        except Exception as e:
            logging.exception(e)
            raise e

    def check_password_hash(self, given_password: str) -> bool:
        """
        Checks if password hash is the same with the provided by the user password
        :return: Whether password hashes are the same
        :rtype: boolean
        :raises Exception: For every error
        """
        try:
            return bcrypt.checkpw(given_password.encode(), self.password)
        except Exception as e:
            logging.exception(e)
            raise e
