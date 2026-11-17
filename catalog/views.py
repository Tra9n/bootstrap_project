from django.views.generic import ListView, DetailView, TemplateView
from .models import Product

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products' 

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

class CategoryTemplateView(TemplateView):
    template_name = 'catalog/category.html'

class CatalogTemplateView(TemplateView):
    template_name = 'catalog/catalog.html'