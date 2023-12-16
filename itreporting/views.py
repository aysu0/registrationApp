from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import CreateView, ListView, FormView, DetailView
from .models import Module, Registration
from .forms import ContactForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django. contrib import messages


def home(request):
    daily_course = {'course': Group.objects.all(), 'title' : 'Course List'}
    return render(request, 'itreporting/home.html', daily_course)

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'})

def module(request):
    daily_report = {'modules': Module.objects.all(), 'title': 'Add a module'}
    return render(request, 'itreporting/module_form.html', daily_report)

def modulelist(request):
    course = Group.objects.get(id = request.data.get('fk'))
    daily_module = {'modules': Module.objects.filter(id = course.id), 'title': 'Modules Registered'}
    return render(request, 'itreporting/modulelist.html', daily_module)

class PostListView(ListView):  
    model = Module
    template_name = 'itreporting/modulelist.html'
    content_object_name = 'models'
    ordering = ['name']

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        course = Group.objects.get(id = self.kwargs.get('fk'))
        context.update({'course': course, 'modules': course.module_set.all()})

        return context

class PostCreateView(CreateView):
    model = Module
    fields = ['name', 'code', 'credit', 'category', 'description', 'availability' ]
    def form_valid(self, form):
        form.instance = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = Module

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registrations = Registration.objects.filter(module = self.object)
        context.update({'title': 'Contact Us', 'registrations': registrations})
        
        return context

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'itreporting/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context.update({'title': 'Contact Us'})
        return context
    
    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'Successfully sent the enquiry')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Unable to send the enquiry') 
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.path
    

# def register_modules(request):
#     user_courses = request.user.groups.all()
#     available_modules = Module.objects.filter(courses__in=user_courses)
    
#     context = {
#         'user_courses': user_courses,
#         'available_modules': available_modules,
#     }
    
#     return render(request, 'register_modules.html', context)