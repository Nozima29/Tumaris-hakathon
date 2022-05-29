from django.urls import path
from favorites.views import FavoritesView, add_to_favorites


urlpatterns = [
    path('', FavoritesView.as_view(), name='favorites'),
    path('add/<int:id>/', add_to_favorites, name='add'),
]
