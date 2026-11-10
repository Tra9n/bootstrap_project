from django.shortcuts import render, get_object_or_404
from .models import Product

def home_view(request):
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {'products': products})

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def contacts_view(request):
    return render(request, 'catalog/contacts.html')

def category_view(request):
    return render(request, 'catalog/category.html')

def catalog_view(request):
    return render(request, 'catalog/catalog.html')