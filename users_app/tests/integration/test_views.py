from django.test import TestCase
from django.urls import reverse


class SignUpSuccessfully(TestCase):

    def setUp(self):
        url = reverse('users_app:signup')
        credentials = {'email': 'new_user@gmail.com',
                       'password1': 'r4nd0mp4ssw0rd',
                       'password2': 'r4nd0mp4ssw0rd',
                       }

        self.response = self.client.post(url, credentials)

    def test_user_has_been_redirect_to_index(self):
        self.assertRedirects(self.response, reverse('users_app:index'))

    def test_user_is_authenticated(self):
        response = self.client.get(reverse('users_app:index'))
        user_status = response.context.get('user').is_authenticated
        self.assertTrue(user_status)
