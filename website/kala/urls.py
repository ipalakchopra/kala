from django.urls import path
from . import views
from django.http import HttpResponse
from django.contrib import admin

urlpatterns=[
    path('', views.home, name = 'Home'),
    path('about', views.about, name = 'About'),
    path('contact', views.contact, name = 'Contact'),
    path('tracking', views.tracking, name = 'Tracking'),
    path('search', views.search, name = 'Search'),
    path('checkout', views.checkout, name = 'Checkout'),
    path('product/<int:prodid>', views.product, name = 'Product'),
    path('sell/', views.sell, name = 'Sell'),    
]