from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView
from .models import Checkout, Product
from .forms import ProductForm,CheckoutForm
from django.core.mail import message, send_mail
# Create your views here.

def home(request):
    prod = Product.objects.all()  
    print({'prod' : prod}) 
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
            prod = Product.objects.order_by('-id')[:1]
            print({'prod' : prod}) 
            return render(request,'product.html',{'prod':prod[0]}) 
    else:
        form = ProductForm()
    return render(request, 'sell.html', {'form' : form})

def allproducts(request):
    prod = Product.objects.all()   
    return render(request,'allproducts.html',{'prod' : prod})    

def checkout(request,prodid):
    prod = Product.objects.filter(id=prodid)
    
    if request.method == 'POST':
       
        form = CheckoutForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            customer_email = form.cleaned_data['customer_email']
            subject = 'Order Placed!'
            message = 'Your order has been placed'
            send_mail(subject,message,'perseforwork@gmail.com',[customer_email])
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form' : form,'prod':prod[0]})
