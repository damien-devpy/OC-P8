from django.test import TestCase

from users_app.models import User


class UserModelTests(TestCase):

    def test_str_user__return_first_and_lastname_if_exists(self):
        new_user = User(username="username", password="password",
                        first_name="Damien", last_name="Ramelet")
        self.assertEqual(str(new_user),
                         f'{new_user.first_name} {new_user.last_name}')

    def test_str_user_return_username_if_first_and_lastname_are_empty(self):
        new_user = User(username="username", password="password")
        self.assertEqual(str(new_user), f'{new_user.username}')
