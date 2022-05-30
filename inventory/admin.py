from django.contrib import admin
from .models import Employee, Customer, Vendor, Product, Producttype, Category, Transaction, Purchase

# Register your models here.
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(Producttype)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Purchase)

