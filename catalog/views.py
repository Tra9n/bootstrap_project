from django.shortcuts import render

def home_view(request):
    """Контроллер главной страницы."""
    return render(request, 'catalog/home.html')

def contacts_view(request):
    """Контроллер страницы контактов."""
    return render(request, 'catalog/contacts.html')

def category_view(request):
    """Контроллер страницы категории."""
    return render(request, 'catalog/category.html')

def catalog_view(request):
    """Контроллер страницы каталога (заказов)."""
    return render(request, 'catalog/catalog.html')