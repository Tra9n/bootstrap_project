from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('category/', views.CategoryTemplateView.as_view(), name='category'),
    path('catalog/', views.CatalogTemplateView.as_view(), name='catalog'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]