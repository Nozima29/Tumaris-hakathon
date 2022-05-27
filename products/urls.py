from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/', ProductDetailView.as_view(), name='detail'),
    path('categories/', CategoryView.as_view(), name='category'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('post/', PostView.as_view(), name='post'),

]
