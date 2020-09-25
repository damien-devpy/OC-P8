from django.contrib.auth.forms import UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Custom User creation form."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name',
                  'last_name')
        labels = {
            'username': 'Nom d\'utilisateur',
            'password1': 'Mot de passe',
            'password2': 'Confirmez votre mot de passe',
            'email': 'Adresse électronique',
            'first_name': 'Prénom',
            'last_name': 'Nom de famille',
        }
