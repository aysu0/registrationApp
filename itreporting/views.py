from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Welcome'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact Us'})