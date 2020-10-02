from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm


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
            request.session['just_signed_up'] = True
            return redirect('users_app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users_app/signup.html', {'form': form})