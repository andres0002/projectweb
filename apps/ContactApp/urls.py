from django.urls import path
from apps.ContactApp import views

urlpatterns = [
    path('', views.Contact.as_view(), name='Contact')
]