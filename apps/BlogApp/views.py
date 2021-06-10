from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from apps.BlogApp.models  import Post, Category

# Create your views here.

class Blog(ListView):
    model = Post
    template_name = 'BlogApp/Blog.html'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        context['posts'] = self.get_queryset()
        return context

    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template_name, self.get_context_data())

class Category(DetailView):
    model = Category
    template_name = 'BlogApp/Category.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['object'] = self.get_object()
        context['posts'] = Post.objects.filter(categoryPost=self.get_object())
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())