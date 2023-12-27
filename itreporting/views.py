from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic import CreateView, ListView, FormView, DetailView
from .models import Module, Registration
from .forms import ContactForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django. contrib import messages
from users.models import Profile
from users.forms import UserRegisterForm

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
    paginate_by = 3

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
    

@login_required
def register_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    user_groups = request.user.groups.all()

    # Check if user is already registered for the module
    existing_registration = Registration.objects.filter(student=request.user, module=module).exists()

    if existing_registration:
        # If user is already registered, show message and redirect
        messages.info(request, 'You are already registered for this module.')
        return redirect('itreporting:module-detail', pk=module_id)

    # Check if user belongs to any of the groups corresponding to the module's courses
    module_courses = module.courses.all()
    if not any(group in user_groups for group in module_courses):
        # If user doesn't belong to the required group(s), show message and redirect
        messages.error(request, 'You cannot register for modules outside your course.')
        return redirect('itreporting:module-detail', pk=module_id)

    if request.method == 'POST':
        # Create new Registration object
        registration = Registration(student=request.user, module=module)
        registration.save()

        # Add success message
        messages.success(request, 'You have registered to this module successfully!')

    # Redirect to 'modules' URL pattern with pk=module_id
    return redirect('itreporting:module-detail', pk=module_id)

@login_required
def unregister_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    user = request.user

    # Check if the user is registered for the module
    registration = Registration.objects.filter(student=user, module=module).first()

    if not registration:
        # If the user is not registered, show a message and redirect
        messages.info(request, 'You are not registered for this module.')
        return redirect('itreporting:module-detail', pk=module_id)

    if request.method == 'POST':
        # Delete the registration object
        registration.delete()

        # Add a success message
        messages.success(request, 'You have unregistered from this module.')

        # Redirect to the 'module-detail' URL pattern or any other appropriate URL
        return redirect('itreporting:module-detail', pk=module_id)

    # Redirect to the 'module-detail' URL pattern if the request method is not POST
    return redirect('itreporting:module-detail', pk=module_id)

def my_registrations(request):
    user_registrations = Registration.objects.filter(student=request.user)
    context = {'user_registrations': user_registrations}
    return render(request, 'itreporting/myregistrations.html', context)