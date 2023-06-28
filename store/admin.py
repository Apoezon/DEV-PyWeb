from django.contrib import admin
from .models import Category, Products, Discount, Cart, Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Discount)
admin.site.register(Cart)
admin.site.register(Profile)
