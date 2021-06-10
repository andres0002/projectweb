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

class Post(models.Model):
    titlePost = models.CharField(max_length=60)
    contentPost = models.CharField(max_length=60)
    imagePost = models.ImageField(upload_to='media/BlogApp/images')
    authorPost = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryPost = models.ManyToManyField(Category)
    createDatePost = models.DateTimeField(auto_now_add=True)
    updateDatePost = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titlePost

    def get_categoryPost(self):
        return ",".join([str(c) for c in self.categoryPost.all()])
