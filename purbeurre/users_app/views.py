from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
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
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users_app/signup.html', {'form': form})

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

