from django.shortcuts import render

def index(request):
    return render(request, 'users/index.html')

def account(request):
    return render(request, 'users/account.html')
