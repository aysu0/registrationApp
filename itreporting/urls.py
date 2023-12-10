from django.urls import path
from . import views
from .views import PostCreateView

app_name = 'itreporting'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('module/<int:pk>', views.module, name = 'module'), 
    path('modulelist', views.modulelist, name='modules'),

    ]