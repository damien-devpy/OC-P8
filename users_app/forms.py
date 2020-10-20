from django.contrib.auth.forms import UserCreationForm

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

    def clean_email(self):
        return self.cleaned_data['email'].lower()