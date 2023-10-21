from django.contrib import admin
from .models.products import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.service import Service
from .models.partner import Partner


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Service)
admin.site.register(Partner)


# username = admin, email = admin@gmail.com, password = 1234

