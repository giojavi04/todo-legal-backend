import unittest

import json

def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            username='11111111',
            password='123456'
        )),
        content_type='application/json'
    )


if __name__ == '__main__':
    unittest.main()
