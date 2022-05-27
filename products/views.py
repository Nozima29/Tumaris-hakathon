from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

# Create your views here.


class HomeView(TemplateView):
    template_name = 'pages/index.html'


class ProductDetailView(TemplateView):
    template_name = 'pages/detail.html'


class CategoryView(TemplateView):
    template_name = 'pages/category.html'


class BlogView(TemplateView):
    template_name = 'pages/blog.html'


class PostView(TemplateView):
    template_name = 'pages/post.html'
