from django.db import models
from datetime import date
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