from django.contrib import admin
from favorites.models import Favorites, FavoriteItems
# Register your models here.

admin.site.register(Favorites)
admin.site.register(FavoriteItems)
