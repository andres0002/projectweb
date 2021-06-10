from django.urls import path
from apps.ProjectWebApp import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home')
]