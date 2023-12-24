from django.urls import path
from . import views
from .views import PostCreateView, ContactFormView, PostDetailView, PostListView

app_name = 'itreporting'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact/', ContactFormView.as_view(), name = 'contact'),
    path('modulelist/<int:fk>', PostListView.as_view(), name='modules'),
    path('module/<int:pk>', PostDetailView.as_view(), name = 'module-detail'), 
    path('register_module/<int:module_id>/', views.register_module, name='register_module'),
    ]
