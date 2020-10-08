from django.contrib.auth import login
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
        try:
            mail_exist = User.objects.get(email=request.POST['email'].lower())
        except User.DoesNotExist:
            mail_exist = None

        if form.is_valid() and not mail_exist:
            user = form.save()
            login(request, user)
            request.session['just_signed_up'] = True
            return redirect('users_app:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users_app/signup.html', {'form': form})
