from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    nameCategory = models.CharField(max_length=60)
    createDateCategory = models.DateTimeField(auto_now_add=True)
    updateDateCategory = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.nameCategory

class Product(models.Model):
    nameProduct = models.CharField(max_length=60)
    imageProduct = models.ImageField(upload_to='media/StoreApp/images')
    priceProduct = models.FloatField()
    availableProduct = models.BooleanField(default=True)
    authorProduct = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryProduct = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.nameProduct

    def get_categoryProduct(self):
        return ", ".join([str(c) for c in self.categoryProduct.all()])