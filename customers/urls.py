from django.urls import path
from customers.views import register, login


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
