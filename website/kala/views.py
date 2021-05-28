from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView
from kala.models import Product
from .forms import ProductForm
# Create your views here.

def home(request):
    prod = Product.objects.all()   
    return render(request,'home.html',{'prod' : prod})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def tracking(request):
    return render(request,'tracking.html')

def search(request):
    return render(request,'search.html')

def checkout(request):
    return render(request,'checkout.html')

def product(request,prodid):
    prod = Product.objects.filter(id=prodid)
    return render(request,'product.html',{'prod':prod[0]}) 

def sell(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return HttpResponse('successfully uploaded')
    else:
        form = ProductForm()
    return render(request, 'sell.html', {'form' : form})

def allproducts(request):
    prod = Product.objects.all()   
    return render(request,'allproducts.html',{'prod' : prod})    