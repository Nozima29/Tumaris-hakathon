from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView


# Create your views here.
from products.models import Products, Category
from shop.models import Inventory


class HomeView(ListView):
    model = Inventory
    context_object_name = 'inventories'
    template_name = 'pages/index.html'

    def get(self, request):
        if request.GET.get('search'):
            keywrd = request.GET.get('search')
            category = Category.objects.filter(name__startswith=keywrd)
            shop = Inventory.objects.filter(name__startswith=keywrd)
            products = Products.objects.filter(type__category__in=category)
            context = {'categories': category,
                       'shops': shop, 'products': products}
            return render(request, 'pages/category.html', context=context)
        return render(request, self.template_name)


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'pages/detail.html'

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        product = Products.objects.get(id=obj.id)
        others = Products.objects.filter(
            type=product.type).exclude(id=product.id)
        context = {'product': product, 'others': others}
        return context


class CategoryView(TemplateView):
    template_name = 'pages/category.html'

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        shops = Inventory.objects.all()
        for category in categories:
            category.counter = category.type.all().count()
        products = Products.objects.all().order_by('-views')

        return {'categories': categories, 'shops': shops, 'products': products}


class BlogView(TemplateView):
    template_name = 'pages/blog.html'


class PostView(TemplateView):
    template_name = 'pages/post.html'
