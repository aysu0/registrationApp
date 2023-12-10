from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView
from .models import Module
from django.contrib.auth.models import Group


# Create your views here.

def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact Us'})

def module(request):
    daily_report = {'modules': Module.objects.all(), 'title': 'Add a module'}
    return render(request, 'itreporting/module_form.html', daily_report)

def modulelist(request):
    daily_module = {'modules': Module.objects.all(), 'title': 'Modules Registered'}
    return render(request, 'itreporting/modules.html', daily_module)

class PostCreateView(CreateView):
    model = Module
    fields = ['name', 'code', 'credit', 'category', 'description', 'availability' ]
    def form_valid(self, form):
        form.instance = self.request.user
        return super().form_valid(form)
    
