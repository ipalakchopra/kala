#from website.kala.views import product
from django.db import models
from datetime import date, datetime, time
from django.db.models.fields import EmailField
# Create your models here.
class Product(models.Model):
    id = models.AutoField
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length=50, default='')
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length = 300)
    pub_date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="static/images",default='')
    
    def __str__(self):
        return self.product_name

class Checkout(models.Model):
    id = models.AutoField
    customer_name = models.CharField(max_length = 100)
    customer_email = models.EmailField()
    product_id = models.IntegerField(default=0)
    payment_choice = (
        ('Cash on Delivery','Cash on Delivery'),
        ('Credit/Debit Card','Credit/Debit Card'),
        ('UPI','UPI')
    )
    payment_mode = models.CharField(max_length=50, choices=payment_choice)
    order_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.customer_name