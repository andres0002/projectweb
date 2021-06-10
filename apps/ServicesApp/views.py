from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from apps.ServicesApp.models import Service 

# Create your views here.

class Services(ListView):
    model = Service
    template_name = 'ServicesApp/Services.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        context['services'] = self.get_queryset()
        return context

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())