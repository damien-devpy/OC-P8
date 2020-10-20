from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'users_app/index.html')


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
