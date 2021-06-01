from django import forms
from django.forms import fields
from .models import Product,Checkout

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'price', 'desc', 'image']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['customer_name','customer_email','payment_mode']
        