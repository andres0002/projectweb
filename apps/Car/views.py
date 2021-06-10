from django.shortcuts import render, redirect
from apps.Car.car import Car
from apps.StoreApp.models import Product

# Create your views here.

def add_product(request, id):
    car = Car(request)
    product = Product.objects.filter(id=id).first()
    car.add(product)
    return redirect('store:Store')

def delete_product(request, id):
    car = Car(request)
    product = Product.objects.filter(id=id).first()
    car.delete(product)
    return redirect('store:Store')

def substract_product(request, id):
    car = Car(request)
    product = Product.objects.filter(id=id).first()
    car.substract_product(product)
    return redirect('store:Store')

def clean_car(request):
    car = Car(request)
    car.clean_car()
    return redirect('store:Store')