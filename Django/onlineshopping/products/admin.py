from django.contrib import admin

from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
