from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'uuid': fields.String(required=True, description='user uuid'),
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'name': fields.String(required=True, description='user name'),
        'last_name': fields.String(required=True, description='user last_name'),
        'phone_number': fields.String(required=True, description='user phone_number'),
        'status': fields.String(required=True, description='user status')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
