from django.contrib import admin

# Register your models here.
from .models import Product, Checkout

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    def display_id(self, obj):
        return obj.id

class CheckoutAdmin(admin.ModelAdmin):
    readonly_fields = ['id']

    def display_id(self, obj):
        return obj.id


admin.site.register(Product,ProductAdmin)
admin.site.register(Checkout,CheckoutAdmin)