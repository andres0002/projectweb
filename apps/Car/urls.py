from django.urls import path
from apps.Car.views import *

urlpatterns = [
    path('add_product/<int:id>/', add_product, name='add_product'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('substract_producto/<int:id>/', substract_product, name='substract_product'),
    path('clean_car/', clean_car, name='clean_car')
]