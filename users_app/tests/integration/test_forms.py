from django.shortcuts import reverse
from django.test import TestCase
from django.utils.encoding import smart_str

from users_app.models import User


class SignUpFormTest(TestCase):

    def setUp(self):
        existing_user = User.objects.create(email="user@mail.com", password="password")

    def test_signup_with_existing_mail_adress_with_upper_case_does_not_allow_signup(self):
        url = reverse('users_app:signup')
        data = {"email": "User@mail.CoM", "password1": "password", "password2": "password"}

        response = self.client.post(url, data)

        assert "Un objet Utilisateur avec ce champ Adresse électronique existe déjà." in smart_str(response.content)
