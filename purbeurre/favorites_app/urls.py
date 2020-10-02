from django.urls import path

from . import views

app_name = 'favorites_app'

urlpatterns = [
    path('', views.Favorites.as_view(), name='favorites'),
]
