from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('createDateCategory', 'updateDateCategory')
    list_display = ['nameCategory', 'createDateCategory', 'updateDateCategory']
    list_filter = ('nameCategory',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('createDatePost', 'updateDatePost')
    list_display = ['titlePost', 'contentPost', 'imagePost', 'authorPost', 'get_categoryPost','createDatePost', 'updateDatePost']
    list_filter = ('authorPost', 'categoryPost')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)