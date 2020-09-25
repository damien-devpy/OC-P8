from django.test import TestCase
from django.urls import reverse, resolve
from users_app.forms import CustomUserCreationForm
from users_app.models import User
from users_app.views import index, signup


class IndexViewTest(TestCase):

    def setUp(self):
        url = reverse('users_app:index')
        self.response = self.client.get(url)

    def test_index_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_url_match_index_view(self):
        index_view = resolve('/')
        self.assertEqual(index_view.func, index)

    def test_base_template_contain_csrf_token_for_search_form(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class SignUpViewTest(TestCase):

    def setUp(self):
        url = reverse('users_app:signup')
        self.response = self.client.get(url)

    def test_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_match_signup_view(self):
        signup_view = resolve('/signup/')
        self.assertEqual(signup_view.func, signup)

    def test_signup_return_expected_form(self):
        self.assertIsInstance(self.response.context.get('form'),
                              CustomUserCreationForm)

    def test_signup_template_contain_two_crsf_token(self):
        # Expect two csrf token
        # One from the search_form in base.html
        # Another one from the signup form
        csrf_token_count = self.response.getvalue().count(
            b'csrfmiddlewaretoken')
        self.assertEqual(csrf_token_count, 2)


class SignUpSuccessfully(TestCase):

    def setUp(self):
        url = reverse('users_app:signup')
        credentials = {'username': 'a_new_user',
                       'password1': 'r4nd0mp4ssw0rd',
                       'password2': 'r4nd0mp4ssw0rd',
                       }

        self.response = self.client.post(url, credentials)

    def test_user_has_been_redirect_to_index(self):
        self.assertRedirects(self.response, reverse('users_app:index'))

    def test_user_has_been_created(self):
        new_user = User.objects.get(username='a_new_user')
        self.assertTrue(new_user)

    def test_user_is_authenticated(self):
        response = self.client.get(reverse('users_app:index'))
        user_status = response.context.get('user').is_authenticated
        self.assertTrue(user_status)
