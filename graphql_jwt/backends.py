from .settings import jwt_settings
from .shortcuts import get_user_by_token
from .utils import get_credentials


class JSONWebTokenBackend:

    def authenticate(self, request=None, **kwargs):
        if request is None or getattr(request, '_jwt_token_auth', False):
            return None

        token = get_credentials(request, **kwargs)

        if token is not None:
            return get_user_by_token(token, request)

        return None

    def get_user(self, user_id):
        return jwt_settings.JWT_GET_USER_BY_NATURAL_KEY_HANDLER(user_id)
