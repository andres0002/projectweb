from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from apps.StoreApp.models import Product, Category

# Create your views here.

class Store(ListView):
    model = Product
    template_name = 'StoreApp/Store.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        context['products'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class Category(DetailView):
    model = Category
    template_name = 'StoreApp/Category.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['object'] = self.get_object()
        context['products'] = Product.objects.filter(categoryProduct=self.get_object()) 
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())