import unittest

import datetime
import uuid

from app.main import db
from app.main.model.user import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            uuid=str(uuid.uuid4()),
            email='test@test.com',
            password='test',
            name='Javier',
            last_name='Montalvo',
            phone_number='0987634456',
            username='1723454344',
            created_at=datetime.datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = User(
            uuid=str(uuid.uuid4()),
            email='test@test.com',
            password='test',
            name='Javier',
            last_name='Montalvo',
            phone_number='0987634456',
            username='1723454344',
            created_at=datetime.datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8") ) == 1)


if __name__ == '__main__':
    unittest.main()

