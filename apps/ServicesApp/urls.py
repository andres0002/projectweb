from django.urls import path
from apps.ServicesApp import views

urlpatterns = [
    path('', views.Services.as_view(), name='Services')
]