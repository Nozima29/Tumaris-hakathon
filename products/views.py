from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Category
from shop.models import Inventory
# Create your views here.


class HomeView(TemplateView):
    template_name = 'pages/index.html'


class ProductDetailView(TemplateView):
    template_name = 'pages/detail.html'


class CategoryView(TemplateView):
    template_name = 'pages/category.html'

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        shops = Inventory.objects.all()

        return {'categories': categories, 'shops': shops}
