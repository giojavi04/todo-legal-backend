from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'uuid': fields.String(required=False, description='user uuid'),
        'email': fields.String(required=False, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'name': fields.String(required=False, description='user name'),
        'last_name': fields.String(required=False, description='user last_name'),
        'phone_number': fields.String(required=False, description='user phone_number'),
        'status': fields.String(required=False, description='user status')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })
