from django.urls import path
from apps.StoreApp import views

urlpatterns = [
    path('', views.Store.as_view(), name='Store'),
    path('Category/<int:pk>', views.Category.as_view(), name='Category')
]