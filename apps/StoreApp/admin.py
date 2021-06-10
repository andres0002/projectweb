from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('createDateCategory', 'updateDateCategory')
    list_display = ['nameCategory', 'createDateCategory', 'updateDateCategory']
    list_filter = ('nameCategory', )

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nameProduct', 'imageProduct', 'priceProduct', 'availableProduct', 'authorProduct', 'get_categoryProduct']
    list_filter = ('availableProduct', 'authorProduct', 'categoryProduct')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin) 
