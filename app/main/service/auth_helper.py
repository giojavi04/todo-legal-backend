from app.main.model.user import User
from ..service.blacklist_service import save_token
from typing import Dict, Tuple


class Auth:

    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # fetch the user data
            user = User.query.filter_by(username=data.get('username')).first()
            if user and user.check_password(data.get('password')):
                auth_token = User.encode_auth_token(user.id)
                if auth_token:
                    return user, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'La información ingresada, no se encuentra en el sistema.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'status': user.status,
                        'registered_on': str(user.created_at)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
