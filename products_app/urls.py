from django.urls import path

from . import views

app_name = 'products_app'

urlpatterns = [
    path('<int:product_id>/', views.substitute, name='substitute'),
    path('product/<int:product_id>/', views.product, name='product')
]
