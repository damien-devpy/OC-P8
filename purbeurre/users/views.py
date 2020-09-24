from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'users/index.html')

def account(request):
    return render(request, 'users/account.html')

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
