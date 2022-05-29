from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', homepage, name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/register/', ProductRegisterView.as_view(),
         name='product-register'),
    path('categories/', CategoryView.as_view(), name='category'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('post/', PostView.as_view(), name='post'),
]
