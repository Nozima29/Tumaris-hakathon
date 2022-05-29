from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/register/', ProductRegisterView.as_view(),
         name='product-register'),
    path('categories/', CategoryView.as_view(), name='category'),
    path('categories/<slug>/', CategoryView.as_view(), name='category-search'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('post/', PostView.as_view(), name='post'),
    path('contact/', ContactView.as_view(), name='contact'),
]
