from django.test import TestCase

from users_app.models import User


class UserModelTests(TestCase):

    def test_str_user_return_username_if_exists(self):
        new_user = User(username="username", email="random.email@mail.com", password="password")
        self.assertEqual(str(new_user),
                         f'{new_user.username}')

    def test_str_user_return_email_if_first_and_lastname_are_empty(self):
        new_user = User(email="random.email@mail.com", password="password")
        self.assertEqual(str(new_user), f'{new_user.email}')
