from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver


@receiver(user_logged_in)
def display_message_logged_in(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS,
                         'Vous êtes maintenant connecté.')


@receiver(user_logged_out)
def display_message_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.SUCCESS,
                         'Vous avez été déconnecté.')
