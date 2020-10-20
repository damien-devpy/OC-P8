from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import User


def index(request):
    context = {}
    if request.session.get('just_signed_up'):
        context.update({'just_signed_up': True})
        request.session['just_signed_up'] = False

    return render(request, 'users_app/index.html', context)


def account(request):
    return render(request, 'users_app/account.html')


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Vous êtes inscrit avec succès.')
            return redirect('users_app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users_app/signup.html', {'form': form})

def credits(request):
    return render(request, 'users_app/credits.html')
