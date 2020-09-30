from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import EmailValidator
from django import forms
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Custom User creation form."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        labels = {
            'password1': 'Mot de passe',
            'password2': 'Confirmez votre mot de passe',
        }

class CustomAuthenticationForm(AuthenticationForm):
    """Custom authentication form.

    Turn username field to email field.

    """

    username = forms.EmailField(label="Adresse électronique", validators=[EmailValidator()], widget=forms.TextInput(attrs={'autofocus': True}))