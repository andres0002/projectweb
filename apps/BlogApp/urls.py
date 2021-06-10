from django.urls import path
from apps.BlogApp import views

urlpatterns = [
    path('', views.Blog.as_view(), name='Blog'),
    path('Category/<int:pk>', views.Category.as_view(), name='Category')
]