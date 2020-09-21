from django.test import TestCase

from users.models import User


class UserModelTests(TestCase):

    def test_user_object_are_pretty_printed(self):
        new_user = User(username="username", password="password",
                        first_name="Damien", last_name="Ramelet")
        self.assertEqual(str(new_user), 'Damien Ramelet')
