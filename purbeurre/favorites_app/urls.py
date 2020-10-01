from django.urls import path
from . import views

app_name = 'favorites_app'

urlpatterns = [
    path('', views.favorites, name='favorites'),
]