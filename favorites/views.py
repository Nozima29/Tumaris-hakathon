from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from products.models import Products
from favorites.models import Favorites, FavoriteItems
# Create your views here.


class FavoritesView(TemplateView):
    template_name = 'pages/basket.html'

    def get_context_data(self, **kwargs):
        total_price = 0
        discount_price = 0
        if self.request.user:
            items = FavoriteItems.objects.filter(
                favorite__customer__user=self.request.user)
        else:
            items = []

        if items:
            favorite = Favorites.objects.filter(
                customer__user=self.request.user).first()
            discount_price = favorite.total_discount
            total_price = favorite.total_price
        return {'items': items, 'discount_price': discount_price, 'total': total_price, 'count': items.count()}


def add_to_favorites(request, id=None):
    if id:
        prod = Products.objects.get(id=id)
    favorite, _ = Favorites.objects.get_or_create(customer__user=request.user)
    FavoriteItems.objects.create(favorite=favorite, product=prod)

    return redirect('favorites')
