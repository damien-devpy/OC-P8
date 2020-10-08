from django.urls import path
from search_app.views import ResultsView

app_name = 'search_app'
urlpatterns = [
    path('', ResultsView.as_view(), name='results'),
]
