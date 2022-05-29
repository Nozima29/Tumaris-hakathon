from typing import Type
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView, ListView
from django.db.models import Q

# Create your views here.
from products.models import Products, Category, Types
from shop.models import Inventory


class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get(self, request):
        if request.GET.get('search'):
            keywrd = request.GET.get('search')
            category = Category.objects.filter(name__startswith=keywrd)
            shop = Inventory.objects.filter(name__startswith=keywrd)
            products = Products.objects.filter(type__category__in=category)
            context = {'categories': category,
                       'shops': shop,
                       'products': products}
            return render(request, 'pages/category.html', context=context)
        inventories = Inventory.objects.all()
        context = {
            'inventories': inventories
        }
        return render(request, 'pages/index.html', context=context)


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'pages/detail.html'

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        product = Products.objects.get(id=obj.id)
        others = Products.objects.filter(
            type=product.type).exclude(id=product.id)
        obj.views += 1
        obj.save()
        context = {'product': product, 'others': others}
        return context


class CategoryView(TemplateView):
    template_name = 'pages/category.html'

    def get_context_data(self, slug=None, **kwargs):
        categories = Category.objects.all()
        shops = Inventory.objects.all()
        for category in categories:
            category.counter = category.type.all().count()
        products = Products.objects.all().order_by('-views')
        if slug:
            qs = Q(type__name=slug) | Q(type__category__name=slug)
            products = products.filter(qs)

        brand = self.request.GET.get('brand')
        if brand:
            products = products.filter(inventory__name=brand)

        return {'categories': categories, 'shops': shops, 'products': products}


class BlogView(TemplateView):
    template_name = 'pages/blog.html'


class PostView(TemplateView):
    template_name = 'pages/post.html'


class ProductRegisterView(TemplateView):
    template_name = 'pages/shop-register-form.html'

    def post(self, request):
        data = request.POST
        shop = Inventory.objects.get(name=data.get('shop'))
        type = Types.objects.get(name=data.get('type'))
        Products.objects.create(
            name=data.get('name'),
            inventory=shop,
            type=type,
            brand=data.get('brand'),
            description=data.get('description', 'none'),
            quantity=data.get('quantity', 1),
            price=float(data.get('price')),
            price_currency='USD',
            discount=float(data.get('discount')),
            collection=data.get('collection', 'none'),
            image=data.get('image')
        )
        return redirect('category')

    def get_context_data(self):
        shops = Inventory.objects.all()
        types = Types.objects.all()

        return {'shops': shops, 'types': types}
