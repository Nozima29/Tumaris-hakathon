from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView


# Create your views here.
from products.models import Products, Category
from shop.models import Inventory


class HomeView(ListView):
    model = Inventory
    context_object_name = 'inventories'
    template_name = 'pages/index.html'


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'pages/detail.html'

class CategoryView(TemplateView):
    template_name = 'pages/category.html'


class BlogView(TemplateView):
    template_name = 'pages/blog.html'


class PostView(TemplateView):
    template_name = 'pages/post.html'
