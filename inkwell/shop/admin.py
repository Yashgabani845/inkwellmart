
from django.contrib import admin
from .models import Category, Customer, Owner, Product, Order, Cart

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Owner)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)


