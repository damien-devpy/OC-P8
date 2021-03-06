from django.contrib.auth.backends import BaseBackend

from .models import User


class CustomBackEnd(BaseBackend):
    """Custom Backend authentification.

    Authenticate against email and password.

    """

    def authenticate(self, request, **kwargs):
        email = kwargs.get('username')
        password = kwargs.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
